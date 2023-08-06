import math

regular_int = r'-?\d+'
regular_float = r'-?\d+(?:[\.\,]\d+)?'

def combinations(k:float=0,n:float=0):
    """
    Функция, считающая число сочетаний из n по k

    Args:
        k (float): аргумент k - количество повторений
        n (float): аргумент n - всего элементов

    Returns:
        float: результат применения формулы числа сочетаний
    """
    if k < 0 or n < 0:
        raise ValueError("ERROR: one or more argument's values are less than 0")
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
