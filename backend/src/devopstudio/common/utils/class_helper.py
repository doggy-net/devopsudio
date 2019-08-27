import inspect
import sys


def get_local_classes(module_name, target_class):
    local_clses = []
    for name, obj in inspect.getmembers(sys.modules[module_name]):
        if inspect.isclass(obj) and issubclass(obj, target_class) \
                and obj.__module__ == module_name:
            local_clses(obj)
    return local_clses
