import hashlib
import inspect
import pickle
from functools import wraps
from pathlib import Path


def slug(data):
    return hashlib.md5(pickle.dumps(data)).hexdigest()


class PickleFSSerializer:
    def load(self, path):
        with open(path, "rb") as f:
            obj = pickle.load(f)
            return obj

    def save(self, path, obj):
        with open(path, "wb") as dill_file:
            pickle.dump(obj, dill_file)


class FSCache:
    def __init__(self, path: Path, key_function=slug, keys=None):
        self.path = Path(path)
        self.key_function = key_function
        self.serializer = PickleFSSerializer()
        self.path.mkdir(exist_ok=True)
        self.keys = keys

    def __call__(self, f):
        def temp(*args, **kwargs):
            if self.keys:
                kwargs = {k: v for k, v in kwargs.items() if k in self.keys}
            fn = self.path / self.key_function(kwargs)
            if fn.exists():
                return self.serializer.load(fn)
            else:
                ret = f(*args, **kwargs)
            self.serializer.save(fn, ret)
            return ret

        return temp
