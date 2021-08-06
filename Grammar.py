class Grammar:
    par = ['RPAR', 'NUM', 'LPAR']
    plus = ['NUM', '+', 'NUM']
    minus = ['NUM', '-', 'NUM']
    multi = ['NUM', '*', 'NUM']
    div = ['NUM', '/', 'NUM']
    foo = ["FOO", "RPAR"]
    prod_priority = ["par", "multi", "div", "plus", "minus", "foo"]
    all_prod = {"par": ['LPAR', 'NUM', 'RPAR'], "multi": ['NUM', 'MUL', 'NUM'], "div": ['NUM', 'DIV', 'NUM'], "plus": [
        'NUM', 'PLS', 'NUM'], "minus": ['NUM', 'MIN', 'NUM'], "foo": ["FOO", "NUM", "RPAR"]}
