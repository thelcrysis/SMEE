import math
from typing import *


class MathFunctions:
    def __init__(self) -> None:
        self.functions = {'sin(': math.sin, 'cos(': math.cos,
                          'tan(': math.tan, 'sqrt(': math.sqrt}

    @staticmethod
    def is_title_viable(foo_title: str) -> bool:
        if foo_title[-1] == '(' and foo_title[:-1].isalpha():
            return True
        return False

    def add_function(self, title: str, foo) -> None:
        assert MathFunctions.is_title_viable(title)
        self.functions[title] = foo

    def add_functions(self, title_function) -> None:
        for key in title_function.keys():
            assert MathFunctions.is_title_viable(key)
            if key in self.functions:
                raise TypeError(f"{key} is already a function.")
            value = title_function[key]
            self.functions[key] = value
