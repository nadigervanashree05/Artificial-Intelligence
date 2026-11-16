import itertools
import re

def evaluate(expr, model):
    expr = expr.replace("<->", " == ")
    expr = expr.replace("->", " <= ")
    expr = expr.replace("^", " and ")
    expr = expr.replace("v", " or ")

    expr = re.sub(r'~(\w+)', r'(not \1)', expr)

    for sym, val in model.items():
        expr = re.sub(r'\b' + sym + r'\b', str(val), expr)

    return eval(expr)


def tt_entails(kb, query, symbols):
    entails = True

    print("A | B | C | KB | Query | KB => Query")
    print("-----------------------------------")

    for values in itertools.product([True, False], repeat=len(symbols)):
        model = dict(zip(symbols, values))

        kb_val = evaluate(kb, model)
        query_val = evaluate(query, model)

        result = (not kb_val) or query_val

        if kb_val and not query_val:
            entails = False

        row = ['T' if v else 'F' for v in values]
        print(" | ".join(row), "|",
              'T' if kb_val else 'F', "|",
              'T' if query_val else 'F', "|",
              'T' if result else 'F')

    if entails:
        print("\nKB entails Query")
    else:
        print("\nKB does NOT entail Query")


kb = "(A v C) ^ (B v ~C)"
symbols = ["A", "B", "C"]

queries = ["A", "C", "A -> B", "B v C"]

for query in queries:
    print("\nQuery:", query)
    tt_entails(kb, query, symbols)
    print("-----------------------------")