"""
    2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


import random


def swich_pos(numbers):
    max_el_ind = 0
    min_el_ind = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max_el_ind]:
            max_el_ind = i
        if numbers[i] < numbers[min_el_ind]:
            min_el_ind = i
    numbers[max_el_ind], numbers[min_el_ind] = numbers[min_el_ind], numbers[max_el_ind]

if __name__ == '__main__':
    numbers = [random.randint(0, 1000) for _ in range(0, 10)]

    print(numbers)
    swich_pos(numbers)
    print(numbers)
