from numbers import Real


def multiply(a=None, b=None):

    if a is None or b is None:
        raise Exception("a or b cannot be null")

    if not isinstance(a, Real) and not isinstance(b, Real):
        raise Exception("a & b must be numbers")

    return a * b
