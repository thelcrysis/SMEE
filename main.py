from SMEE import Evaluator

def main():
    evaluator = Evaluator()
    print("Math expression:",end='')
    math_expr = str(input())
    print(f"{math_expr} = {evaluator.eval_expr(math_expr)}")

if __name__ == '__main__':
    main()