from typing import *
from Token import Token


class Lexical:
    operators = ['+', '-', '(', ')', '/', '*']
    pre_negative_number_op = ['+', '-', '(', '/', '*']
    numbers = [str(i) for i in range(10)]
    space = ' '
    float_point = '.'
    negative = '-'
    eligible_chars = operators + numbers + [space, float_point]
    EOL = '$'

    #TODO: add common constants
    #TODO: add support for negative numbers
    @staticmethod
    def is_numerical(input_: str) -> bool:
        for char in list(input_):
            if char not in [*Lexical.numbers, Lexical.float_point, Lexical.negative]:
                return False
        return True

    @staticmethod
    def tokenize(input_: str) -> List[str]:
        result: List[str] = []
        stack = []
        input_ += Lexical.EOL
        op_last = True
        for char in input_:
            if char == Lexical.EOL:
                if stack:
                    result.append(''.join(stack))
                continue
            if char not in Lexical.eligible_chars:
                raise ValueError("Syntax error")
            if char == Lexical.space:
                continue
            # last condition takes current - sign as part of negative number
            if char in Lexical.numbers or char == Lexical.float_point or (op_last and char == Lexical.negative):
                op_last = False
                stack.append(char)
                continue
            if char in Lexical.operators:
                print(char, stack)
                if char in Lexical.pre_negative_number_op and op_last == False:
                    op_last = True
                elif stack:
                    op_last = False
                result.append(''.join(stack))
                stack.clear()
                result.append(char)
                continue
        return result

    @staticmethod
    def parse(input_: str) -> List[Token]:
        text_2_type = {'+': 'PLS', '-': 'MIN', '*': 'MUL',
                       '/': 'DIV', '(': 'LPAR', ')': 'RPAR'}

        text_tokens = Lexical.tokenize(input_)
        result_tokens = []

        for no, tkn in enumerate(text_tokens):
            if Lexical.is_numerical(tkn):
                new_token = Token(tkn, "NUM", no)
            else:
                new_token = Token(tkn, text_2_type[tkn], no)
            result_tokens.append(new_token)

        return result_tokens
