from typing import List


class FlowError(Exception):
    pass


class MissingAnnotation(Exception):
    pass


class InternalTypeError(Exception):
    pass


class WrongType(TypeError):
    def __init__(self, *args, wrong_values: List[dict]):
        self.wrong_values = wrong_values
        super().__init__(*args)


class TypeNotMapped(Exception):
    pass


class IteratorItemWarning(Warning):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return repr(self.message)
