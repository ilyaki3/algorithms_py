"""
    Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
    Вывести на экран это число и сумму его цифр.
"""


def max_digit_sum(n: str) -> None:
    numbers = n.split()
    digit_sum = [0] * len(numbers)

    for j in range(len(numbers)):
        for k in range(len(numbers[j])):
            digit_sum[j] += int(numbers[j][k])

    max_sum = 0
    for i in digit_sum:
        if max_sum < i:
            max_sum = i
    print(max_sum)


if __name__=='__main__':
    # n = input("Введите натуральные числа через пробел\n>>> ")
    n = "2345 876 5678 9876 5678 987655 5678987 76567 9879 6765"
    max_digit_sum(n)