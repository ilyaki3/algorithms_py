"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)
"""


def backward_rec(n: int) -> int:
    result = 0
    while n != 0:
        result = result * 10 + n % 10
        n = n // 10
    return result


if __name__ == '__main__':
    n = int(input("Сформируем из введенного числа обратное\n>>> "))
    print(backward_rec(n))

