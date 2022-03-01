"""
    3. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
        Сами минимальный и максимальный элементы в сумму не включать.
"""


def sum_between_min_max(numbers):
    max_el_ind = 0
    min_el_ind = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max_el_ind]:
            max_el_ind = i
        if numbers[i] < numbers[min_el_ind]:
            min_el_ind = i

    sum_between = 0
    if min_el_ind < max_el_ind:
        for i in range(min_el_ind + 1, max_el_ind):
            sum_between += numbers[i]
    else:
        for i in range(max_el_ind + 1, min_el_ind):
            sum_between += numbers[i]
    return sum_between



if __name__ == '__main__':
    print(sum_between_min_max([4, 5, 3, 100, 7, 9, 2]))
    print(sum_between_min_max([4, 5, 3, 1, 7, 9, 200]))
