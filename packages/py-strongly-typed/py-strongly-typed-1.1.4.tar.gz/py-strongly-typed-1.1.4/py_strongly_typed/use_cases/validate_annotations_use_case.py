from typing import Any, Tuple, Union

from py_strongly_typed.contracts import IValidateAnnotationsUseCase
from py_strongly_typed.exceptions import FlowError, MissingAnnotation, InternalTypeError, WrongType


class ValidateAnnotationsUseCase(IValidateAnnotationsUseCase):
    def _set_kwargs_validated(self, value: bool):
        if not isinstance(value, bool):
            raise InternalTypeError('value must be a boolean.')

        self.__kwargs_validated = value

    def _validate_arguments_has_types(self):
        missing = [var for var in self._func.__code__.co_varnames if var != 'self' and var not in self._annotations]
        if missing:
            raise MissingAnnotation(f'{missing} is missing type annotations.')

    def _get_expected_type_name(self, expected_type: Any):
        name: str = getattr(expected_type, '__qualname__', None)
        if not name:
            name = str(expected_type)

        if name.upper() == 'UNION':
            types = str(expected_type).replace('typing.Union', '').replace('[', '').replace(']', '').split(',')
            name = f"{name.capitalize()}{types}"

        return name.replace('"', '').replace("'", '')

    def _insert_wrong_field(self, field: str, expected_type: Any, provided: Any):
        self._wrong_fields.append({
            "field": field,
            "expected": self._get_expected_type_name(expected_type),
            "provided": provided.__class__.__name__
        })

    def _validate_expected_type(self, expected_type: Any, value: Any) -> bool:
        if expected_type == Any:
            return True

        if self._ignore_float_and_integer_difference is True:
            if isinstance(expected_type, (int, float)) and self._ignore_float_and_integer_difference is True:
                expected_type = Union[int, float]

        return isinstance(value, expected_type)

    def _validate_args(self, *args):
        if not self.__kwargs_validated:
            raise FlowError('Kwargs must be validated before args.')

        for index, arg in enumerate(args):
            expected_type = list(self._annotations.values())[index]
            is_valid = self._validate_expected_type(expected_type=expected_type, value=arg)

            if not is_valid:
                self._insert_wrong_field(field=list(self._annotations.keys())[index],
                                         expected_type=expected_type,
                                         provided=arg)

    def _validate_kwargs(self, **kwargs):
        for key, value in kwargs.items():
            expected_type = self._annotations.pop(key)
            is_valid = self._validate_expected_type(expected_type=expected_type, value=value)

            if not is_valid:
                self._insert_wrong_field(field=key, expected_type=expected_type, provided=value)

        self._set_kwargs_validated(True)

    def execute(self, *args, **kwargs) -> Tuple[Tuple, dict]:
        self._validate_arguments_has_types()
        self._validate_kwargs(**kwargs)
        self._validate_args(*args)

        if self._wrong_fields:
            message = f"{self._func.__qualname__} arguments received " \
                      f"wrong types: \n" + "\n".join([str(field) for field in self._wrong_fields])
            raise WrongType(message, wrong_values=self._wrong_fields)

        return args, kwargs
