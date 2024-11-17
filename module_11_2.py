# Домашнее задание по теме "Интроспекция"

# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.

import inspect

class MyClass:
    def __init__(self):
        self.number = 1

    def any_func(self, x):
        x = x**3

def introspection_info(obj):
    info = {}
    info[1] = type(obj)
    info[2] = dir(obj)
    info[3] = inspect.getmodule(obj)
    info[4] = callable(obj)
    info[5] = inspect.isclass(obj)

    return info
my_obj = MyClass()

obj_info = introspection_info(my_obj)
print(obj_info)
