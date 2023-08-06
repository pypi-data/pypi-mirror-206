from abc import ABC, abstractmethod


class IValidateAnnotationsUseCase(ABC):
    def __init__(self, func, ignore_float_and_integer_difference: bool):
        self._func = func
        self._annotations = self._func.__annotations__.copy()
        self._wrong_fields = []
        self._ignore_float_and_integer_difference = ignore_float_and_integer_difference
        self.__kwargs_validated = False

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError()
