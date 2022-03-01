"""
    4. В одномерном массиве целых чисел определить два наименьших элемента.
        Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""


import random


def min_two_el(arr):
    if len(arr) < 3:
        return arr

    first =  arr[0]
    second = first
    for i in range(1, len(arr)) or second >= arr[i]:
        if second >= arr[i]:
            second = arr[i]
        if first >= arr[i]:
            second = first
            first = arr[i]

    return first, second



if __name__ == '__main__':
    numbers = [random.randint(0, 1000) for _ in range(0, 10)]
    print(numbers)
    print(min_two_el(numbers))
