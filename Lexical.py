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
        if input_ == '':
            return False
        # input '-' is not a number
        if len(input_) == 1 and input_ == '-':
            return False
        for char in list(input_):
            if char not in [*Lexical.numbers, Lexical.float_point, Lexical.negative]:
                return False
        return True

    #TODO: add a**b
    @staticmethod
    def tokenize(input_: str) -> List[str]:
        result: List[str] = []
        stack = []
        input_ += Lexical.EOL
        op_last = True
        all_chars = ''

        function_name = ''

        for char in input_:
            all_chars += char
            # checking for EOL and space
            if char == Lexical.EOL:
                if stack:
                    result.append(''.join(stack))
                continue
            if char == Lexical.space:
                continue
            
            # fishing for functions 
            if char.isalpha():
                function_name += char
                continue
            if function_name != '' and char == '(':
                function_name += '('
                result.append(function_name)
                function_name = ''
                continue
            # fishing for numerical values
            # last condition takes current - sign as part of negative number
            if char in Lexical.numbers or char == Lexical.float_point or (op_last and char == Lexical.negative):
                op_last = False
                stack.append(char)
                continue

            if char in Lexical.operators:
                if char in Lexical.pre_negative_number_op and op_last == False:
                    op_last = True
                elif stack:
                    op_last = False
                if Lexical.is_numerical(''.join(stack)):
                    result.append(''.join(stack))
                    stack.clear()
                    result.append(char)
                else:
                    result.append(char)
                    stack.clear()
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
            # math functions
            elif tkn != '(' and tkn[-1] == '(':
                new_token = Token(tkn, "FOO", no)
            else:
                new_token = Token(tkn, text_2_type[tkn], no)
            result_tokens.append(new_token)
        print(result_tokens)
        return result_tokens
