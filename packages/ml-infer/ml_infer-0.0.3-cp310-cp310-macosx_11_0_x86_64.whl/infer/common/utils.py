import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

from torch._C import DictType, ListType, Node, TensorType, TupleType, Value

if TYPE_CHECKING:
    from torch._C import JitType


def is_tensor_or_tensor_container(jit_type: "JitType") -> bool:
    if isinstance(jit_type, TensorType):
        return True
    if isinstance(jit_type, ListType):
        return is_tensor_or_tensor_container(jit_type.getElementType())
    if isinstance(jit_type, DictType):
        return is_tensor_or_tensor_container(jit_type.getValueType())
    if isinstance(jit_type, TupleType):
        return any(is_tensor_or_tensor_container(t) for t in jit_type.elements())
    return False


def is_tensor_container(jit_type: "JitType") -> bool:
    if isinstance(jit_type, ListType):
        return is_tensor_or_tensor_container(jit_type.getElementType())
    if isinstance(jit_type, DictType):
        return is_tensor_or_tensor_container(jit_type.getValueType())
    if isinstance(jit_type, TupleType):
        return any(is_tensor_or_tensor_container(t) for t in jit_type.elements())
    return False


@dataclass
class Source:
    file_name: str
    line_no: int


def get_source(node_or_value: Node | Value) -> Source | None:
    if isinstance(node_or_value, Node):
        node = node_or_value
    elif isinstance(node_or_value, Value):
        node = node_or_value.node()
    else:
        raise TypeError(f"Expected Node or Value, got {type(node_or_value)}")
    if not node.sourceRange() or not (match := re.search(r"File \"(.+?)\", line (\d+)", str(node.sourceRange()))):
        return None
    file, line_no = match.groups()
    return Source(file, int(line_no))
