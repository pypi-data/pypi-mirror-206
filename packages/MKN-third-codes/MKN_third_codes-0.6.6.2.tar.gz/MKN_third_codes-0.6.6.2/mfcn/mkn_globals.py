import math

regular_int = r'-?\d+'
regular_float = r'-?\d+(?:[\.\,\/]\d+)?'

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

def to_float_values(array: list):
    """
    Перевод каждой строки из входного массива в формат float

    Args:
        array (list(string)): массив строк, являющихся float-ами
    
    Returns:
        list(float): массив float
    """
    for i in range(0, len(array)):
        if "," in array[i]:
            ind = array[i].index(",")
            array[i] = float(array[i][:ind]+"."+array[i][ind+1:])
        elif "/" in array[i]:
            ind = array[i].index("/")
            array[i] = int(array[i][:ind])/int(array[i][ind+1:])
        else:
            array[i] = float(array[i])
    return array
