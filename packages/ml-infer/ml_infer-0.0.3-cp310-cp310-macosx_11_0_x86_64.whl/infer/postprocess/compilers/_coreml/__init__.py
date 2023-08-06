try:
    import coremltools  # noqa, pylint: disable=import-error

except ModuleNotFoundError as e:
    from infer.utils.platform import is_apple_silicon

    if is_apple_silicon():
        raise ModuleNotFoundError("CoreML is not installed; install using `pip install ml-infer[coreml]") from e
    else:
        raise ValueError("CoreML is not supported on non-Apple Silicon devices") from e
