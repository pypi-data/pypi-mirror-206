from typing import Type

from py_strongly_typed.contracts import IValidateAnnotationsUseCase
from py_strongly_typed.use_cases.validate_annotations_use_case import ValidateAnnotationsUseCase
from py_strongly_typed.decorators import typed_function


class TypedClass:
    typing_validator: Type[IValidateAnnotationsUseCase] = ValidateAnnotationsUseCase
    type_all_methods: bool = True

    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if not callable(attr) or self.type_all_methods is False:
            return attr

        return typed_function(attr)

    def __new__(cls, *args, **kwargs):
        core = cls.typing_validator(func=cls.__init__)
        core.execute(*args, **kwargs)

        return super().__new__(cls)


class TypedInit(TypedClass):
    type_all_methods = False
