"""
    Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
    Вывести на экран это число и сумму его цифр.
"""


def max_sum_of_digits():
    numbers = input('Введите натуральные числа через пробел\n>>> ').split()
    max_num = 0
    max_sum = 0
    for el in numbers:
        current_number = list(map(int, el))
        if sum(current_number) >= max_sum:
            max_num, max_sum = el, sum(current_number)
    print(f'Наибольшее по сумме цифр число {max_num}\nСумма его цифр = {max_sum}')


if __name__ == '__main__':
    max_sum_of_digits()