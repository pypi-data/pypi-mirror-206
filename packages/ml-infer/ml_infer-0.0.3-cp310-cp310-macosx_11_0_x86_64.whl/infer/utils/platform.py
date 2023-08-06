import functools
import platform
import re
import shutil


@functools.lru_cache
def is_apple_silicon() -> bool:
    machine = platform.machine()
    return bool(re.search("arm64", machine))


@functools.lru_cache
def has_cuda() -> bool:
    return shutil.which("nvcc") is not None
