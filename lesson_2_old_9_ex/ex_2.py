"""
    Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_even_odd_num():

    number = input('Считаем четные и нечетные цифры числа.\n'
                    'Ведите натуральное число:\n>>> ')

    if number.isdigit():
        numbers_list = list(number)
    else:
        print('Ошибка ввода')
        return

    even_count = 0
    odd_count = 0
    for el in range(len(numbers_list)):
        if int(el) & 1:
            odd_count += 1
        else:
            even_count += 1

    print(f'В числе {number}\nНечетных цифр: {odd_count}\nЧетных цифр: {even_count}')


if __name__ == '__main__':
    count_even_odd_num()