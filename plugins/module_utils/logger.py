import functools
import logging

# Configure logging without `encoding` if Python version < 3.9
logging.basicConfig(
    level=logging.INFO,
    filename="/tmp/fmcansible.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def get_detailed_representation(obj):
    """Helper function to get detailed information about an object."""
    if hasattr(obj, '__dict__'):
        return f"{obj.__class__.__name__} with attributes {obj.__dict__}"
    elif hasattr(obj, '__repr__'):
        return repr(obj)
    else:
        return str(obj)

def log_this(func):
    """Decorator to log function name, args, and kwargs with detailed object representation."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        # Expand each argument using `get_detailed_representation`
        detailed_args = [get_detailed_representation(arg) for arg in args]
        # detailed_kwargs = {k: get_detailed_representation(v) for k, v in kwargs.items()}

        logging.info(f"Calling {func_name} with args: {detailed_args},")#kwargs: {detailed_kwargs}")

        return func(*args, **kwargs)
    return wrapper