"""
    Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
    выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def validation(text):
    try:
        n = int(input(text))
        return n
    except ValueError:
        print('Ошибка ввода')
        return

def equation():
    print('Программа проверяет, что для множества натуральных чисел\n'
          'выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.')
    n = validation('Введите число n\n>>> ')
    if n == None: return

    a = 0
    for i in range(n):
        a += i + 1
    b = n * (n + 1) / 2
    print(f'1+2+...+n = {a}\nn(n+1)/2 = {int(b)}')


if __name__ == '__main__':
    equation()