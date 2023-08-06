import collections
import warnings
from typing import Any, Tuple, Union, List, Dict

from py_strongly_typed.contracts import IValidateAnnotationsUseCase
from py_strongly_typed.exceptions import FlowError, MissingAnnotation, InternalTypeError, WrongType, TypeNotMapped, \
    IteratorItemWarning
from py_strongly_typed.utils import is_generic, is_union


class ValidateAnnotationsUseCase(IValidateAnnotationsUseCase):
    def execute(self, *args, **kwargs) -> Tuple[Tuple, dict]:
        self._validate_arguments_has_types()
        self._validate_kwargs(**kwargs)
        self._validate_args(*args)

        if self._wrong_fields:
            message = f"{self._func.__qualname__} arguments received " \
                      f"wrong types: \n" + "\n".join([str(field) for field in self._wrong_fields])
            raise WrongType(message, wrong_values=self._wrong_fields)

        return args, kwargs

    def _set_kwargs_validated(self, value: bool):
        if not isinstance(value, bool):
            raise InternalTypeError('value must be a boolean.')

        self.__kwargs_validated = value

    def _validate_arguments_has_types(self):
        missing = [var for var in self._func.__code__.co_varnames if var != 'self' and var not in self._annotations]
        if missing:
            raise MissingAnnotation(f'{missing} is missing type annotations.')

    def _get_expected_type_name(self, expected_type: Any):
        if is_generic(expected_type):
            return str(expected_type).replace('typing.', '')

        return getattr(expected_type, '__qualname__', None)

    def _insert_wrong_field(self, field: str, expected_type: Any, provided: Any):
        representation = provided.__class__.__name__
        if not is_union(expected_type) and is_generic(expected_type) and isinstance(provided, expected_type.__origin__):
            representation = f'{representation.capitalize()}{self._provided_args}'.replace("'", '')

        self._wrong_fields.append({
            "field": field,
            "expected": self._get_expected_type_name(expected_type),
            "provided": representation
        })

    def _validate_expected_type(self, expected_type: Any, value: Any) -> bool:
        if expected_type == Any:
            return True

        if hasattr(expected_type, '__args__') and expected_type.__origin__ != Union:
            return self._validate_generic(generic=expected_type, value=value)

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

    def _insert_provided_arg(self, provided_arg: type):
        self._provided_args.append(provided_arg.__qualname__)

    def _extend_provided_args(self, provided_args: List[type]):
        self._provided_args.extend([arg.__qualname__ for arg in provided_args])

    def _validate_generic(self, generic, value: Any) -> bool:
        father_expected_type = generic.__origin__
        if not isinstance(value, father_expected_type):
            return False

        if father_expected_type == collections.abc.Iterator:
            if generic.__args__:
                warnings.warn('Iterator items will be not validated, only Iterator as itself.', IteratorItemWarning)
            return True

        instance_father = father_expected_type()
        if isinstance(instance_father, (Tuple, List)):
            return self._validate_generic_list_or_tuple(generic=generic, value=value)

        elif isinstance(instance_father, Dict):
            return self._validate_dict(generic=generic, value=value)

        raise TypeNotMapped('It was not possible to validate this type. Please report this problem opening '
                            'an issue on: %s' % 'https://github.com/chrislcontrol/py-strongly-typed/issues')

    def _validate_generic_list_or_tuple(self, generic, value: Union[List, Tuple]) -> bool:
        is_valid = True
        for value_child in value:
            if type(value_child).__qualname__ not in self._provided_args:
                self._insert_provided_arg(type(value_child))

            if is_valid and not isinstance(value_child, generic.__args__):
                is_valid = False

        return is_valid

    def _validate_dict(self, generic, value: Dict):
        is_valid = True
        expected_key_type, expected_value_type = generic.__args__
        for key, value in value.items():
            self._extend_provided_args([type(key), type(value)])
            if is_valid and not isinstance(key, expected_key_type) or not isinstance(value, expected_value_type):
                is_valid = False

        return is_valid
