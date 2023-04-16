import warnings

# Does not raise a type error
warnings.warn(1)

# Raises a type error
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", "test")
    warnings.warn(1)