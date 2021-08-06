from SMEE import Evaluator
from MathFunctions import MathFunctions
def kvadrat(a:float):
    return a*a

def main():
    evaluator = Evaluator()
    evaluator.add_function('sqr(', kvadrat)    
    print("Math expression:",end='')
    # math_expr = str(input())
    math_expr = '2+sqr()2)'
    print(f"{math_expr} = {evaluator.eval_expr(math_expr)}")


if __name__ == '__main__':
    main()