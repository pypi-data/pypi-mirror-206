from typing import Type

from py_strongly_typed.contracts import IValidateAnnotationsUseCase
from py_strongly_typed.use_cases.validate_annotations_use_case import ValidateAnnotationsUseCase
from py_strongly_typed.decorators import typed_function


class TypedClass:
    typing_validator: Type[IValidateAnnotationsUseCase] = ValidateAnnotationsUseCase
    type_all_methods: bool = True
    ignore_float_and_integer_difference: bool = True

    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if not callable(attr) or self.type_all_methods is False:
            return attr

        return typed_function(attr, ignore_float_and_integer_difference=self.ignore_float_and_integer_difference)

    def __new__(cls, *args, **kwargs):
        core = cls.typing_validator(func=cls.__init__,
                                    ignore_float_and_integer_difference=cls.ignore_float_and_integer_difference)
        core.execute(*args, **kwargs)

        return super().__new__(cls)


class TypedInit(TypedClass):
    type_all_methods = False
