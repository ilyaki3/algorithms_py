"""
    1. В диапазоне натуральных чисел от 2 до 99 определить,
        сколько из них кратны каждому из чисел в диапазоне от 2 до 9
"""


def multiplicity(numbers):
    count = 0
    for num in numbers:
        flag = True
        for d in range(2, 10):
            if num % d != 0:
                flag = False
                break
        if flag == True: count += 1

    return count


if __name__ == '__main__':
    numbers = (i for i in range(2, 100))
    print(multiplicity(numbers))
