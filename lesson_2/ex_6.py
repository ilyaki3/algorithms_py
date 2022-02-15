"""
    В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
    не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше
    введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано,
    то вывести загаданное число.randint(0,100)
"""


from random import randint


def validation(text):
    try:
        n = int(input(text))
        return n
    except ValueError:
        print('Ошибка ввода')
        return

def guess_the_number():
    print('В программе генерируется случайное целое число от 0 до 100. '
          'Вы должны его отгадать не более чем за 10 попыток.\n'
          'После каждой неудачной попытки вы узнаете больше или '
          'меньше введенное вами число, чем то, что загадано.\n')

    hidden_number = randint(0,100)
    attempts = 0
    while True:
        user_number = validation(('Введите число:\n>>> '))
        if user_number == None: return

        attempts += 1
        if user_number == hidden_number:
            print(f'\nПоздравляем! Вы отгадали число {hidden_number}\nКолличество попыток: {attempts}')
            return
        elif user_number < hidden_number:
            print('Загаданное число больше.')
        else:
            print('Загаданное число меньше.')


if __name__ == '__main__':
    guess_the_number()
