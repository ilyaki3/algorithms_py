"""
    Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    Количество элементов (n) вводится с клавиатуры.
"""


def validation(text):
    try:
        n = int(input(text))
        if n < 0:
            raise ValueError
        return n
    except ValueError:
        print('Ошибка ввода')
        return


def row_sum():
    n = validation('Найдём сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...\n'
                      'Введите колличество элементов n\n>>> ')
    if n == None: return

    result = 0
    item = 1
    row = ''
    for i in range(n):
        result += item
        row += ' ' + str(item)
        item /= -2
    print(f'Сумма ряда {row} равна {result}')



if __name__ == '__main__':
    row_sum()