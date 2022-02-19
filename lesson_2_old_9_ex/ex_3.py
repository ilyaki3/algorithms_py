"""
    Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
    Например, если введено число 3486, то надо вывести число 6843.
"""


def reversed_num():

    number = input('Сформируем из введенного числа обратное\n'
                    'Ведите число:\n>>> ')

    if number.isdigit():
        print(number[::-1])

    # Другой вариант
    # for el in range(0, len(number), -1):
    #     result = ''.join(el)
    #     print(result)
    #     return

    else:
        print('Ошибка ввода')
        return


if __name__ == '__main__':
    reversed_num()

