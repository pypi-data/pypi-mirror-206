import inspect


def instanceclass(cls):
    orig_init = cls.__init__
    cls.instance = None

    def __init__(self, *args, **kws):
        orig_init(self, *args, **kws)
        cls.instance = self

        class_methods = inspect.getmembers(self, predicate=inspect.ismethod)
        instance_methods = list(filter(lambda x: hasattr(x[1], 'instance_method'), class_methods))
        [setattr(cls, method[0], method[1].instance_method.__get__(self, self.__class__))
         for method in instance_methods]

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls.instance is None:
            return cls(*args, **kwargs)
        else:
            return cls.instance

    cls.__init__ = __init__
    cls.get_instance = get_instance

    return cls



def instancemethod(method):
    def wrapper(*args, **kwargs):
        raise ReferenceError("Parent instance class is not instantiated")

    wrapper.instance_method = method
    return wrapper