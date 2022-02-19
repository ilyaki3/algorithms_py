"""
    Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
    Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
    должна завершаться, а должна запрашивать новые данные для вычислений.
    Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
    Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
    сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о
    невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""


def validation_args(text):
    try:
        arg = int(input(text))
    except ValueError:
        arg = 'Ошибка ввода\n'
    return arg


def validation_operator(text):
    operator_list = ['+', '-', '*', '/', '0']
    try:
        operator = input(text)
        if operator not in operator_list:
            raise ValueError
    except ValueError:
        operator = 'Ошибка ввода\n'
    return operator


def calculations(arg1, operator, arg2):
        if operator == '+':
            print(f'{arg1} + {arg2} = {round(arg1 + arg2, 4)}\n')
        if operator == '-':
            print(f'{arg1} - {arg2} = {round(arg1 - arg2, 4)}\n')
        if operator == '*':
            print(f'{arg1} * {arg2} = {round(arg1 * arg2, 4)}\n')
        if operator == '/':
            print(f'{arg1} / {arg2} = {round(arg1 / arg2, 4)}\n')


def calculator():
    print('Программа складывает, вычитает, умножает или делит два числа\n'
          'Введите числа и знак операции.\n'
          'Завершение программы выполнится при вводе символа 0 в качестве знака операции.')

    while True:
        arg1 = validation_args('Введите первое число:\n>>> ')
        if isinstance(arg1, str):
            print(arg1)
            continue

        operator = validation_operator("Введите знак операции ('+', '-', '*', '/' или '0' для выхода):\n>>> ")
        if operator == '0':
            print('Работа программы завершена.')
            break
        if operator == 'Ошибка ввода\n':
            print(operator)
            continue

        arg2 = validation_args('Введите второе число:\n>>> ')
        if isinstance(arg2, str):
            print(arg2)
            continue
        if operator == '0' and arg2 == 0:
            print('Ошибка ввода. Деление на ноль\n')
            continue

        calculations(arg1, operator, arg2)


if __name__ == "__main__":
    calculator()
