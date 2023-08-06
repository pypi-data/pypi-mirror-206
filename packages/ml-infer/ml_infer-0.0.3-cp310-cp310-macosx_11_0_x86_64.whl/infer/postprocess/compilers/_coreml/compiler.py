from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import coremltools as cm
import numpy as np
import torch
from torch import Tensor

from infer.postprocess.compilers.base import Compiler
from infer.postprocess.compilers.utils import get_arr
from infer.postprocess.graph import PostprocessGraph, PostprocessNode
from infer.postprocess.handlers.utils import rectify_dim

MODEL_SPEC_NAME = "network.mlmodel"


@dataclass
class CoreMLConfig:
    use_exact_array_input_shape_mapping: bool = field(default=True)
    use_rank_5_image_shape_mapping: bool = field(default=True)


def assert_not_none(i: int | None) -> int:
    assert i is not None, "CoreML compiler doesn't support broadcasting shapes yet"
    return i


def ones(i: int) -> list[int]:
    return [1] * i


def get_static_shape(shape: Iterable[int | None] | torch.Size) -> cm.models.datatypes.Array:
    """Converts a dynamic input shape to a static rank-5 shape.

    Args:
        shape: The dynamic input shape

    Returns:
        The rank-5 shape expected by CoreML.
    """

    shape_concrete = [assert_not_none(i) for i in shape]
    rank = len(shape_concrete)
    assert 1 <= rank <= 5, f"Invalid {rank=}"

    if rank == 1:
        (b,), (t, c, h, w) = shape_concrete, ones(4)
    elif rank == 2:
        (b, c), (t, h, w) = shape_concrete, ones(3)
    elif rank == 3:
        (b, h, w), (t, c) = shape_concrete, ones(2)
    elif rank == 4:
        (b, c, h, w), (t,) = shape_concrete, ones(1)
    else:
        (b, c, t, h, w) = shape_concrete

    return cm.models.datatypes.Array(t, b, c, h, w)


def normalize_dim(dim: int, shape: Iterable[int | None] | torch.Size) -> int:
    """Normalizes a dimension to the static rank-5 dimension.

    Args:
        dim: The dimension to normalize
        shape: The dynamic input shape

    Returns:
        The normalized rank-5 dimension.
    """

    shape = list(shape)
    rank = len(shape)
    assert 1 <= rank <= 5, f"Invalid {rank=}"
    dim = rectify_dim(dim, rank)

    def choose_dim(choices: list[int]) -> int:
        assert 0 <= dim <= len(choices), f"Dimension is out-of-bounds: {dim}"
        return choices[dim]

    if rank == 1:
        return choose_dim([1])
    if rank == 2:
        return choose_dim([1, 2])
    if rank == 3:
        return choose_dim([1, 3, 4])
    if rank == 4:
        return choose_dim([1, 2, 3, 4])
    return choose_dim([0, 1, 2, 3, 4])


def convert_to_static_shape(t: Tensor) -> Tensor:
    static_shape = get_static_shape(t.shape)
    return t.view(static_shape.dimensions)


class CoreMLCompiler(Compiler):
    """Defines a translator for generating a CoreML package."""

    def __init__(self, graph: PostprocessGraph, config: CoreMLConfig | None = None) -> None:
        super().__init__(graph)

        self.config = CoreMLConfig() if config is None else config

    def add_node(self, node: PostprocessNode, builder: cm.models.neural_network.NeuralNetworkBuilder) -> None:
        match node.op:
            case "prim::Param" | "prim::Return":
                pass
            case "aten::conv2d":
                in_name, out_name = node.inputs[0], node.outputs[0]
                assert (conv_data := node.data.conv2d) is not None
                kernel, bias = get_arr(conv_data.weight), get_arr(conv_data.bias)
                builder.add_convolution(
                    name=node.name,
                    kernel_channels=kernel.shape[1] * conv_data.groups,
                    output_channels=kernel.shape[0],
                    height=kernel.shape[2],
                    width=kernel.shape[3],
                    stride_height=conv_data.stride[0],
                    stride_width=conv_data.stride[1],
                    border_mode="same",
                    groups=conv_data.groups,
                    W=kernel,
                    b=bias,
                    has_bias=bias is not None,
                    is_deconv=False,
                    output_shape=get_static_shape(node.get_shape(out_name)),
                    input_name=in_name,
                    output_name=out_name,
                    dilation_factors=conv_data.dilation,
                    padding_top=conv_data.padding[0] // 2,
                    padding_bottom=(conv_data.padding[0] + 1) // 2,
                    padding_left=conv_data.padding[1] // 2,
                    padding_right=(conv_data.padding[1] + 1) // 2,
                    same_padding_asymmetry_mode="BOTTOM_RIGHT_HEAVY",
                )
            case "aten::linear":
                in_name, out_name = node.inputs[0], node.outputs[0]
                assert (linear_data := node.data.linear) is not None
                weight = linear_data.weight.unflatten(-1, (-1, 1, 1))
                kernel, bias = get_arr(weight), get_arr(linear_data.bias)
                builder.add_convolution(
                    name=node.name,
                    kernel_channels=kernel.shape[1],
                    output_channels=kernel.shape[0],
                    height=1,
                    width=1,
                    stride_height=1,
                    stride_width=1,
                    border_mode="same",
                    groups=1,
                    W=kernel,
                    b=bias,
                    has_bias=bias is not None,
                    is_deconv=False,
                    output_shape=get_static_shape(node.get_shape(out_name)),
                    input_name=in_name,
                    output_name=out_name,
                    dilation_factors=(1, 1),
                    padding_top=0,
                    padding_bottom=0,
                    padding_left=0,
                    padding_right=0,
                    same_padding_asymmetry_mode="BOTTOM_RIGHT_HEAVY",
                )
            case "aten::clamp":
                in_name, out_name = node.inputs[0], node.outputs[0]
                assert (clamp_data := node.data.clamp) is not None
                builder.add_clip(
                    name=node.name,
                    input_name=in_name,
                    output_name=out_name,
                    min_value=clamp_data.min_val,
                    max_value=clamp_data.max_val,
                )
            case "inference::cat":
                in_names, out_name = node.inputs, node.outputs[0]
                assert (concat_data := node.data.concat) is not None
                builder.add_concat_nd(
                    name=node.name,
                    input_names=in_names,
                    output_name=out_name,
                    axis=normalize_dim(concat_data.dim, node.get_shape(out_name)),
                    interleave=False,
                )
            case "aten::reshape":
                in_name, out_name = node.inputs[0], node.outputs[0]
                assert (reshape_data := node.data.reshape) is not None
                builder.add_reshape_static(
                    name=node.name,
                    input_name=in_name,
                    output_name=out_name,
                    output_shape=reshape_data.shape,
                )
            case "aten::transpose":
                in_name, out_name = node.inputs[0], node.outputs[0]
                assert (transpose_data := node.data.transpose) is not None
                dim_a, dim_b = transpose_data.dim_a, transpose_data.dim_b
                node_shape = node.get_shape(in_name)
                permutation = list(range(len(get_static_shape(node_shape).dimensions)))
                dim_a, dim_b = normalize_dim(dim_a, node_shape), normalize_dim(dim_b, node_shape)
                permutation[dim_a], permutation[dim_b] = permutation[dim_b], permutation[dim_a]
                builder.add_transpose(
                    name=node.name,
                    axes=permutation,
                    input_name=in_name,
                    output_name=out_name,
                )
            case "aten::matmul":
                in_names, out_name = node.inputs, node.outputs[0]
                builder.add_batched_mat_mul(
                    name=node.name,
                    input_names=in_names,
                    output_name=out_name,
                    transpose_a=True,
                    transpose_b=True,
                )
            case "aten::add" | "aten::mul":
                out_name = node.outputs[0]
                assert (eltwise_data := node.data.eltwise) is not None
                opt_lhs_name: str | None
                opt_rhs_name: str | None
                if eltwise_data.lhs is None and eltwise_data.rhs is None:
                    opt_lhs_name, opt_rhs_name = node.inputs
                elif eltwise_data.lhs is None:
                    (opt_lhs_name,), opt_rhs_name = node.inputs, None
                elif eltwise_data.rhs is None:
                    opt_lhs_name, (opt_rhs_name,) = None, node.inputs
                else:
                    opt_lhs_name, opt_rhs_name = None, None
                lhs: int | float | str | None = eltwise_data.lhs if opt_lhs_name is None else opt_lhs_name
                rhs: int | float | str | None = eltwise_data.rhs if opt_rhs_name is None else opt_lhs_name
                assert lhs is not None and rhs is not None
                if isinstance(lhs, str) and isinstance(rhs, (int, float)):
                    lhs, rhs = rhs, lhs
                if isinstance(lhs, (int, float)) and isinstance(rhs, str):
                    lhs_constant_value = np.full((1,), lhs)
                    builder.add_load_constant(
                        name=node.name + "_const",
                        output_name=lhs,
                        constant_value=lhs_constant_value,
                        shape=[1, 1, 1],
                    )
                if isinstance(lhs, str) and isinstance(rhs, str):
                    builder.add_elementwise(
                        name=node.name,
                        input_names=[lhs, rhs],
                        output_name=out_name,
                        mode="ADD" if node.op == "aten::add" else "MULTIPLY",
                    )
                else:
                    raise NotImplementedError(f"{node.op=} not implemented for two concretes\n{node.source_string}")
            case "aten::softmax":
                in_name, out_name = node.inputs[0], node.outputs[0]
                assert (softmax_data := node.data.softmax) is not None
                static_shape = get_static_shape(node.get_shape(out_name))
                sm_dim = normalize_dim(softmax_data.dim, node.get_shape(out_name))
                exp_dim = len(static_shape.dimensions) - 3
                if sm_dim != exp_dim:
                    permutation = list(range(len(static_shape.dimensions)))
                    permutation[sm_dim], permutation[exp_dim] = permutation[exp_dim], permutation[sm_dim]
                    builder.add_transpose(
                        name=node.name + "_transpose",
                        axes=permutation,
                        input_name=in_name,
                        output_name=node.name + "_transpose",
                    )
                    in_name = node.name + "_transpose"
                builder.add_softmax(
                    name=node.name,
                    input_name=in_name,
                    output_name=out_name,
                )
            case _:
                raise NotImplementedError(f"{node.op=} not implemented\n{node.source_string}")

    def translate(self) -> cm.models.neural_network.NeuralNetworkBuilder:
        self.preprocess()

        # Gets the input and output nodes.
        param_nodes = [node for _, node in self.graph.gen_nodes(op="prim::Param")]
        return_nodes = [node for _, node in self.graph.gen_nodes(op="prim::Return")]
        assert len(param_nodes) == 1 and len(return_nodes) == 1
        input_features = [(o, get_static_shape(param_nodes[0].get_shape(o))) for o in param_nodes[0].outputs]
        output_features = [(i, get_static_shape(return_nodes[0].get_shape(i))) for i in return_nodes[0].inputs]

        builder = cm.models.neural_network.NeuralNetworkBuilder(
            input_features=input_features,
            output_features=output_features,
        )

        nnproto = cm.proto.NeuralNetwork_pb2

        # Updates array input shape mapping configuration.
        if self.config.use_exact_array_input_shape_mapping:
            array_input_mapping = nnproto.NeuralNetworkMultiArrayShapeMapping.Value("EXACT_ARRAY_MAPPING")
        else:
            array_input_mapping = nnproto.NeuralNetworkMultiArrayShapeMapping.Value("RANK5_ARRAY_MAPPING")
        builder.nn_spec.arrayInputShapeMapping = array_input_mapping

        # Updates image shape mapping configuration.
        if self.config.use_rank_5_image_shape_mapping:
            image_input_mapping = nnproto.NeuralNetworkImageShapeMapping.Value("RANK5_IMAGE_MAPPING")
        else:
            image_input_mapping = nnproto.NeuralNetworkImageShapeMapping.Value("RANK4_IMAGE_MAPPING")
        builder.nn_spec.imageInputShapeMapping = image_input_mapping

        for _, node in self.graph.gen_nodes():
            self.add_node(node, builder)

        return builder

    def compile(self, save_dir: Path) -> None:
        # Saves the initial graph.
        self.graph.save(save_dir / "model.graph")

        # Converts the model to a spec, then saves the spec.
        builder = self.translate()

        cm.models.utils.save_spec(builder.spec, save_dir / MODEL_SPEC_NAME)

        # Saves the input spec as well.
        spec = self.graph.get_spec()
        spec.save(save_dir / "input_spec.json")


def compile_graph(graph: PostprocessGraph, save_dir: Path | str) -> None:
    """Short-hand function for calling the compiler.

    Args:
        graph: The graph to compile
        save_dir: Where to save the compiled package
    """

    CoreMLCompiler(graph).compile(Path(save_dir))
