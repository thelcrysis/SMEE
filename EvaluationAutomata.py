from typing import *
from Token import Token
from Grammar import Grammar

class EvalAutomata:
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



    @staticmethod
    def eval(input_: List[Token]):
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
                    #TODO: add some math functions
                    stack.append(pattern_result)
                    typed_stack.append(pattern_result.type)
        
        return float(stack[0].token)
        

