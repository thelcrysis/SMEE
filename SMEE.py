from typing import *
from Lexical import Lexical
from EvaluationAutomata import EvalAutomata
from MathFunctions import MathFunctions


class Evaluator:
    def __init__(self) -> None:
        self.lex = Lexical()
        self.automata = EvalAutomata()

    # modular function addition
    def add_function(self, title: str, foo) -> None:
        self.automata.math_functions.add_function(title, foo)

    def add_functions(self, title_function) -> None:
        self.automata.math_functions.add_function(title_function)

    def eval_expr(self, expr: str) -> float:
        parsed_expr = self.lex.parse(expr)
        return self.automata.eval(parsed_expr)
