from typing import Union


def is_generic(value):
    return hasattr(value, '__args__')


def is_union(value):
    return is_generic(value) and value.__origin__ == Union
