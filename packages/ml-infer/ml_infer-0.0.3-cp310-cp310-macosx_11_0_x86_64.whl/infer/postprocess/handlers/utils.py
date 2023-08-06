from typing import TypeVar

T = TypeVar("T")


def rectify_dim(dim: int | None, rank: int) -> int:
    if dim is None:
        return 0
    return dim if dim >= 0 else rank + dim


def cast_item_not_none(i: T | None) -> T:
    assert i is not None
    return i


def cast_not_none(s: tuple[T | None, ...]) -> tuple[T, ...]:
    return tuple(cast_item_not_none(i) for i in s)
