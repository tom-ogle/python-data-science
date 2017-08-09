import math


def vector_add(v, w):
    """Performs vector addition"""
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """Performs vector subtraction"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """Componentwise sum all vectors"""
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    """Multiplies every element of vector v by constant c"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """Componentwise means of a list of same-sized vectors"""
    n = len(vectors)
    return scalar_multiply(1.0/n, vector_sum(vectors))


def dot_product(v, w):
    """Dot product of two vectors"""
    products = [v_i * w_i for v_i, w_i in zip(v, w)]
    return sum(products)


def sum_of_squares(v):
    """Sum of squares of a vector"""
    return dot_product(v, v)


def magnitude(v):
    """Magnitude (length) of a vector"""
    return math.sqrt(sum_of_squares(v))


def distance(v, w):
    """"""
    magnitude(vector_subtract(v, w))
