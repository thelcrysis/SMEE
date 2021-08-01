from Lexical import Lexical
from EvaluationAutomata import EvalAutomata
class Evaluator:
    def __init__(self) -> None:
        self.lex = Lexical()
        self.automata = EvalAutomata()
    
    def eval_expr(self, expr:str) -> float:
        parsed_expr = self.lex.parse(expr)
        return self.automata.eval(parsed_expr)
