
import os 


def join_path(*paths):
    """Return a path using os specific path seperator."""
    return os.path.join(*paths)
