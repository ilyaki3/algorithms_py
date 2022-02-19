"""
    Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
    Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def digit_count(numbers: str, digit: str) -> None:
    count = 0
    for i in numbers:
        if i == digit:
            count += 1
    print(count)


if __name__=="__main__":
    numbers = input("Введите последовательность чисел\n>>> ")
    digit = input("Введите цифру для подсчета\n>>> ")
    digit_count(numbers, digit)