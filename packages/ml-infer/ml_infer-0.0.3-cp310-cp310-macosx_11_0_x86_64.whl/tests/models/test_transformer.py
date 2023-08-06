import math
from pathlib import Path

import pytest
import torch
from torch import Tensor, nn

from infer.postprocess.compilers.auto import compile_graph, get_engine
from infer.postprocess.generate import generate
from infer.preprocess.init import preprocess_
from infer.utils.tests import assert_dicts_equal


class SelfAttention(nn.Module):
    __constants__ = ["num_heads", "hidden_dims", "norm_scale"]

    def __init__(self, hidden_dims: int, num_heads: int) -> None:
        super().__init__()

        assert hidden_dims % num_heads == 0

        self.num_heads = num_heads
        self.head_dims = hidden_dims // num_heads
        self.norm_scale = 1.0 / math.sqrt(self.head_dims)

        self.q_linear = nn.Linear(hidden_dims, hidden_dims)
        self.v_linear = nn.Linear(hidden_dims, hidden_dims)
        self.k_linear = nn.Linear(hidden_dims, hidden_dims)

        self.out = nn.Linear(hidden_dims, hidden_dims)

    def attention(self, q: Tensor, k: Tensor, v: Tensor) -> Tensor:
        scores = torch.matmul(q, k.transpose(-2, -1)) * self.norm_scale
        scores = torch.softmax(scores, dim=-1)
        output = torch.matmul(scores, v)
        return output

    def forward(self, q: Tensor, k: Tensor, v: Tensor) -> Tensor:
        # Perform linear operation and split into h heads
        k = self.k_linear(k).unflatten(-1, (self.num_heads, self.head_dims))
        q = self.q_linear(q).unflatten(-1, (self.num_heads, self.head_dims))
        v = self.v_linear(v).unflatten(-1, (self.num_heads, self.head_dims))

        # Transpose to get dimensions bs * h * sl * d_model
        k = k.transpose(1, 2)
        q = q.transpose(1, 2)
        v = v.transpose(1, 2)

        # Calculate attention using function we will define next
        scores = self.attention(q, k, v)

        # Concatenate heads and put through final linear layer
        concat = scores.transpose(1, 2).contiguous().flatten(-2)
        output = self.out(concat)

        return output


@pytest.mark.tensorrt
def test_tensorrt_transformer() -> None:
    assert True  # Implement this


@pytest.mark.coreml
def test_coreml_transformer(tmpdir: Path) -> None:
    module = SelfAttention(512, 8)
    module.eval()
    q, k, v = torch.randn(3, 1, 10, 512).unbind(0)
    script_module = preprocess_(module, example_inputs=[(q, k, v)])
    postprocess_graph = generate(script_module)
    spec = postprocess_graph.get_spec()
    input_names, output_name = [i.name for i in spec.inputs], spec.outputs[0].name
    torch_output: dict[str, Tensor] = {output_name: script_module(q, k, v)}

    # Compiles the graph to the temporary directory.
    compile_graph("coreml", postprocess_graph, tmpdir)

    # Loads the compiled graph and runs inference on a single sample.
    engine = get_engine("coreml", tmpdir)
    coreml_output: dict[str, Tensor] = engine({input_names[0]: q, input_names[1]: k, input_names[2]: v})

    # Checks that the engine output matches the Torch output.
    assert_dicts_equal(coreml_output, torch_output)
