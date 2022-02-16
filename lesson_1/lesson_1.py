"""      Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python      """
"""_______________________________________________________________________________________"""

import random

"""
 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


def product_and_sum():
    user_numbers = input('Введите трёхзначное число, для которого нужно вычислить сумму и произведение: \n >>> ')

    num_sum = int(user_numbers[0]) + int(user_numbers[1]) + int(user_numbers[2])
    num_prod = int(user_numbers[0]) * int(user_numbers[1]) * int(user_numbers[2])
    return f'Сумма чисел = {num_sum}\nПроизведение чисел =  {num_prod}'

# print(product_and_sum())


"""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
    Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
"""


def logic_operations():
    a = 5
    b = 6

    print(f'a & b = {a & b}',
          f'a | b = {a | b}',
          f'a ^ b = {a ^ b}',
          f'~a = {~a}',
          f'~b = {~b}',
          f'a << 2 = {a << 2}',
          f'b >> 2 = {b >> 2}', sep='\n')

# logic_operations()


"""
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
"""


def equation():
    coords = input('Введите через пробел координаты точек: (x1 y1 x2 y2)\n>>> ')

    x1, x2, y1, y2 = list(map(int, coords.split()))

    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return f'y = {k}x + {b}'

# print(equation())

"""
4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.

    Для каждого из трех случаев пользователь задает свои границы диапазона.
    Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
    Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""


def generate():
    user_input = input('Введите через пробел что сгенерировать:\n'
                       '[ i - случайное целое число;\n  f - случайное вещественное число;\n  s - случайный символ]'
                       ' и границы [от] и [до]\nНапример: i 10 999\n>>> ')

    gen_mode, limit_from, limit_to = user_input.split()

    if gen_mode == 's':
        limit_from = ord(limit_from)
        limit_to = ord(limit_to)
        return chr(random.randint(limit_from, limit_to))

    elif gen_mode == 'i':
        return random.randint(int(limit_from), int(limit_to))
    elif gen_mode == 'f':
        return round(random.uniform(int(limit_from), int(limit_to)), 3)


"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

def letter_position():
    user_input = input('Введите две буквы через запятую:\n>>> ')
    first, second = user_input.split()

    first_place = ord(first) - 96
    second_place = ord(second) - 96

    letters_between = second_place - first_place

    return f'{first} - {first_place} место\n{second} - {second_place} место\n' \
           f'Букв между ними - {abs(letters_between)}'

# print(letter_position())


"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""


def num_to_letter():
    user_input = input('Введите номер буквы в алфавите:\n>>> ')
    return chr(int(user_input) + 96)

# print(num_to_letter())


"""
7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
    составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
    равнобедренным или равносторонним.
"""


def triangle():
    user_input = input('Введите длины сторон треугольника через пробел:\n>>> ')
    a, b, c = list(map(int, user_input.split()))

    if a + b < c or a + c < b or b + c < a:
        return 'Такой треугольник не может существовать.'
    elif a == b == c:
        return 'Треугольник равносторонний'
    elif a == b or a == c or b == c:
        return 'Треугольник равнобедренный'
    else:
        return 'Треугольник разносторонний'

# print(triangle())


"""
8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""

def is_leap_year():
    year = int(input('Введите год:\n>>> '))

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return f'{year} - Год високосный'
    else:
        return f'{year} - Год не високосный'

# print(is_leap_year())


"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""


def avg_num():
    user_input = input('Введите три разных числа:\n>>> ')
    num_1, num_2, num_3 = list(map(int, user_input.split()))

    if num_2 < num_1 < num_3 or num_2 > num_1 > num_3:
        return f'{num_1} - Среднее'
    if num_1 < num_2 < num_3 or num_1 > num_2 > num_3:
        return f'{num_2} - Среднее'
    if num_2 < num_3 < num_1 or num_2 > num_3 > num_1:
        return f'{num_3} - Среднее'

#     nums = list(set(map(int, user_input.split())))
#     return f'{nums[1]} - Среднее'
#
# print(avg_num())











