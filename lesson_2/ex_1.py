"""
    Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_even_odd_num(n:int) -> None:
    even = 0
    odd = 0
    while n != 0:
        if (n % 10) & 1:
            odd += 1
        else:
            even += 1
        n = n // 10

    print(f'Чётных = {even}, нечетных = {odd}')


if __name__=='__main__':
    n = int(input('Посчитаем четные и нечетные цифры введенного натурального числа.\n>>> '))
    count_even_odd_num(n)

