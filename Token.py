from typing import *


class Token:
    op_types = {"PLS": "+", "MIN": "-", "MUL": "*",
                "DIV": "/", "LPAR": "(", "RPAR": ")"}

    other_types = ['NUM','FOO']

    def __init__(self, token, type_, place) -> None:
        self.token = token
        if type_ not in Token.op_types and type_ not in Token.other_types:
            raise TypeError(f"Type is not in {Token.op_types}")
        self.type = type_
        if place is not None and place < 0 and type(place) != int:
            raise ValueError(f"Place not positive integer.")
        elif place is None:
            self.place = None
        else:
            self.place = int(place)
        

    def __str__(self) -> str:
        return f"{self.token} {self.type} {self.place}"
