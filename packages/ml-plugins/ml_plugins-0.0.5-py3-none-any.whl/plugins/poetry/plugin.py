import functools
from metaflow.includefile import IncludeFile 
from metaflow.exception import MetaflowException


def poetry(path):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            import subprocess
            import sys
            subprocess.run([sys.executable, '-m', 'poetry', 'install'])
            return function(*args, **kwargs)
        return wrapper
    return decorator

@poetry(path="pyproject.toml")
def x():
    print("outer function, using poetry to install fasttext")
    pass

if __name__ == "__main__":
  x()