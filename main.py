"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
        функция, которая принимает N целых чисел,
        и возвращает список квадратов этих чисел
        >>> power_numbers(1, 2, 5, 7)
        [1, 4, 25, 49]
        """
    for n in args:
        if not isinstance(n, int):
            return False

    return [n ** 2 for n in args]





# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    cnt = 0
    del_n = 2
    while del_n < n:
        if n % del_n == 0:
            cnt += 1
            break
        else:
            del_n += 1
    return cnt == 0

def filter_numbers(List_n, Filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """
    for n in List_n:
        if not isinstance(n, int):
            return False

    if Filter == ODD:
        return list(filter(lambda x: x % 2 == 1, List_n))
    elif Filter == EVEN:
        return list(filter(lambda x: x % 2 == 0, List_n))
    elif Filter == PRIME:
        res = []
        for n in List_n:
            if n <= 0:
                continue
            if (is_prime(n)):
                res.append(n)
        return res
    else:
        return False

