def is_variable(x):
    return isinstance(x, str) and x.islower()

def occurs_check(var, expr, subst):
    if var == expr:
        return True
    elif isinstance(expr, list):
        return any(occurs_check(var, e, subst) for e in expr)
    elif expr in subst:
        return occurs_check(var, subst[expr], subst)
    return False

def unify(x, y, subst=None, depth=0):
    if subst is None:
        subst = {}

    indent = " " * depth
    print(indent + f"Unify({x}, {y})")

    if x == y:
        return subst

    elif is_variable(x):
        return unify_var(x, y, subst, depth)

    elif is_variable(y):
        return unify_var(y, x, subst, depth)

    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None

        for a, b in zip(x, y):
            subst = unify(a, b, subst, depth + 1)
            if subst is None:
                return None

        return subst

    else:
        return None

def unify_var(var, x, subst, depth):
    indent = " " * depth

    if var in subst:
        return unify(subst[var], x, subst, depth + 1)

    elif isinstance(x, str) and x in subst:
        return unify(var, subst[x], subst, depth + 1)

    elif occurs_check(var, x, subst):
        print(indent + "Occurs check failed")
        return None

    else:
        subst[var] = x
        return subst


expr1 = ['f', 'X', ['g', 'Y']]
expr2 = ['f', 'b', ['g', 'a']]

print("Starting Unification:\n")

result = unify(expr1, expr2, {})

print("\nFinal Unification Result:", result)