from abc import ABC, abstractmethod


class IValidateAnnotationsUseCase(ABC):
    def __init__(self, func):
        self._func = func
        self._annotations = self._func.__annotations__.copy()
        self._wrong_fields = []
        self._provided_args = []
        self.__kwargs_validated = False

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError()
