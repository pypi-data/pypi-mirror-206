from typing import Callable, Type

from py_strongly_typed import IValidateAnnotationsUseCase
from py_strongly_typed.use_cases.validate_annotations_use_case import ValidateAnnotationsUseCase


def typed_function(func,
                   ignore_float_and_integer_difference: bool = True,
                   typing_validator: Type[IValidateAnnotationsUseCase] = ValidateAnnotationsUseCase) -> Callable:
    def return_func(*args, **kwargs):
        core = typing_validator(func=func, ignore_float_and_integer_difference=ignore_float_and_integer_difference)
        core.execute(*args, **kwargs)
        return func(*args, **kwargs)

    return return_func
