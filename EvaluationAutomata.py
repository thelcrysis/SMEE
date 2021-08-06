from typing import *
from Token import Token
from Grammar import Grammar
from MathFunctions import MathFunctions

class EvalAutomata:
    #TODO: modular math functions need to be tested
    def __init__(self, math_functions:MathFunctions = None) -> None:
        self.math_functions = None
        if math_functions is None:
            self.math_functions = MathFunctions()
        else:
            self.math_functions = math_functions

    @staticmethod
    def pattern_matching(stack:List[Token]):
        for rule in Grammar.prod_priority:
            pattern = Grammar.all_prod[rule]
            for i in range(len(stack)+1):
                if stack[-i:] == pattern:
                    return -i, rule
        return False

    @staticmethod
    def PLUS(data:List[Token]):
        val_a = float(data[0].token)
        val_b = float(data[2].token)
        return Token(str(val_a+val_b),'NUM',None)

    @staticmethod
    def MINUS(data:List[Token]):
        val_a = float(data[0].token)
        val_b = float(data[2].token)
        return Token(str(val_a-val_b),'NUM',None)
    
    @staticmethod
    def PAR(data:List[Token]):
        val = float(data[1].token)
        return Token(str(val),'NUM',None)

    @staticmethod
    def MUL(data:List[Token]):
        val_a = float(data[0].token)
        val_b = float(data[2].token)
        return Token(str(val_a*val_b),'NUM',None)
    
    @staticmethod
    def DIV(data:List[Token]):
        val_a = float(data[0].token)
        val_b = float(data[2].token)
        return Token(str(val_a/val_b),'NUM',None)

    def FOO(self, data:List[Token]):
        for n, token in enumerate(data):
            print(n,':',token)
        available_functions:Dict[str,function] = self.math_functions.functions
        for foo_title in available_functions.keys():
            calculate_function = available_functions[foo_title]
            if foo_title == str(data[0].token):
                val = calculate_function(float(data[1].token))
        return Token(str(val), 'NUM', None)

    def eval(self, input_: List[Token]):
        stack = []
        typed_stack = []
        for token in input_:
            stack.append(token)
            typed_stack.append(token.type)
            while True:
                result = EvalAutomata.pattern_matching(typed_stack)
                if not result:
                    break
                else:
                    place, rule = result
                    data = stack[place:].copy()
                    stack = stack[:place].copy()
                    typed_stack = typed_stack[:place].copy()

                    if rule == 'plus':
                        pattern_result = EvalAutomata.PLUS(data)
                    elif rule == 'minus':
                        pattern_result = EvalAutomata.MINUS(data)
                    elif rule == 'par':
                        pattern_result = EvalAutomata.PAR(data)
                    elif rule == 'multi':
                        pattern_result = EvalAutomata.MUL(data)
                    elif rule == 'div':
                        pattern_result = EvalAutomata.DIV(data)
                    elif rule == 'foo':
                        pattern_result = self.FOO(data)

                    stack.append(pattern_result)
                    typed_stack.append(pattern_result.type)

        return float(stack[0].token)
        

