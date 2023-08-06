try:
    import tensorrt  # noqa: F401

except ModuleNotFoundError as e:
    from infer.utils.platform import has_cuda

    if has_cuda():
        raise ModuleNotFoundError("TensorRT is not installed; install using `pip install ml-infer[tensorrt]") from e
    else:
        raise ValueError("TensorRT is not supported on non-CUDA devices") from e
