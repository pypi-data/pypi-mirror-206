![Supported Python Versions](https://img.shields.io/badge/python-3.5%2B-brightgreen)
![pypi version](https://img.shields.io/pypi/v/py-strongly-typed)
![Last commit](https://img.shields.io/github/last-commit/chrislcontrol/py-strongly-typed)
[![Downloads](https://pepy.tech/badge/py-strongly-typed/month)](https://pepy.tech/project/py-strongly-typed)

What do I need?
===============
- Python (3.5+)


Description
===========

With py-strongly-typed, now typing annotations metters! Use this lib to validate provided args typing.


Be free to contribute with our [GitHub](https://github.com/chrislcontrol/typyd) project.



Get Started
===========

- **Install**

        pip install py-strongly-typed

Usage
===========

-  **Typing classes**

        from py_strongly_typed import TypedClass


        class SomeClass(TypedClass):
            def __init__(self, first_arg: str, second_arg: int):
                self.first_arg = first_arg
                self.second_arg = second_arg
            
            def some_method(*, method_arg: list):
                pass


        instance_class = SomeClass('arg_value', second_arg=1)
        istance_class.some_method(method_arg=[1])

   You can also to set only `__init__` method to be typed doing:
        
        from py_strongly_typed import TypedClass


        class SomeClass(TypedClass):
            type_all_methods: bool = False

            def __init__(self, first_arg: str, second_arg: int):
                self.first_arg = first_arg
                self.second_arg = second_arg
            
            def some_method(*, method_arg: list):
                pass


        instance_class = SomeClass('arg_value', second_arg=1)
        istance_class.some_method(method_arg=[1])

   or:

        from py_strongly_typed import TypedInit


        class SomeClass(TypedInit):
            def __init__(self, first_arg: str, second_arg: int):
                self.first_arg = first_arg
                self.second_arg = second_arg
            
            def some_method(*, method_arg: list):
                pass


        instance_class = SomeClass('arg_value', second_arg=1)
        istance_class.some_method(method_arg=[1])

&nbsp;
-  **Typing function or methods**

   You can also use decorators for methods or functions typing:

         from py_strongly_typed import typed_function
   
         @typed_function
         def some_function(arg: str):
             pass

Objects
===========
- **TypedClass** class
   ``Used to set a class to has typing annotations validated.``


  - **TypedInit** class
  ``Used to set a class to has typing annotations validated on __init__ only.``


- **typed_function** decorator
   ``Used to set a function or method to has typing annotations validated.``


- **IValidateAnnotationsUseCase** abstract class
  ``Interface that should be used to implement custom typing validations.``


- **ValidateAnnotationsUseCase** class (inherit IValidateAnnotationsUseCase)
   ``Default typing validation core.``



Argument options
===========

- **TypedClass and TypedInit**

  - ***typing_validator*** *[Type[IValidateAnnotationsUseCase]]* ***[default=ValidateAnnotationsUseCase]***: 
  `You can provide an custom class that validates typing.`

  - ***type_all_methods*** *[bool]* ***[default=True]***:
  `Defines if all methods of the class will be type validated or only __init__.`

  - ***ignore_float_and_integer_difference*** *[bool]* ***[default=True]***: 
  `If True, providing an integer on a float expected or inverse will be ignored.`


- **@typed_function decorator**

  - ***typing_validator*** *[Type[IValidateAnnotationsUseCase]]*: `You can provide an custom class that validates
  typing.`

  - ***ignore_float_and_integer_difference*** *[bool]*: `If True, providing an integer on a float expected or inverse 
  will be ignored.`


- **IValidateAnnotationsUseCase**
  - ***func*** *[Callable]*: Function that will has be called after typing validation.
  - ***ignore_float_and_integer_difference*** *[bool]*: `If True, providing an integer on a float expected or inverse 
  will be ignored.`


Behavior
===========
   * When an invalid value type is provided, WrongType exception will be raised.
   * When function or method is defined with any argument missing annotation, 
MissingAnnotation will be raised.

Limitations
===========
   * Generics (example: List[str]) are not supported yet.
   * Typing using or operator will validate only first one. Example: providing str or int, 
only str will be considered. To provide more than one expected type, use `|` operator or `Union`.
   * `*args` and `**kwargs` are not supported due to be impossible to provide typing annotations for them 
without Generics.


## License
[MIT](https://choosealicense.com/licenses/mit/)
