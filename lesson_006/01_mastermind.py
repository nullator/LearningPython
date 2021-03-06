# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from mastermind_engine import generate_number, check_number
from termcolor import cprint, colored


def game():
    generate_number()
    res = {'bulls': 0, 'cows': 0}
    n = 0
    while res['bulls'] < 4:
        user_number = input(colored('Введите число: ', color='blue'))
        if check_number(user_number):
            res = check_number(user_number)
            cprint(f"быки - {res['bulls']}, коровы - {res['cows']}", color='yellow')
            n += 1
        else:
            cprint('Некорректный ввод. Число должно состоять из 4 цифр, в числе все цифры должны быть разные',
                   color='red')
    if n == 1:
        cprint(f'Вы отгадали число за {n} ход!', color='green')
    elif n == 2 or n == 3 or n == 4:
        cprint(f'Вы отгадали число за {n} хода!', color='green')
    else:
        cprint(f'Вы отгадали число за {n} ходов!', color='green')


cprint('Правила:', color='red', attrs=['underline'])
cprint('''Компьютер загадывает четырехзначное число, все цифры которого различны
(первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
Игрок вводит четырехзначное число c неповторяющимися цифрами,
компьютер сообщают о количестве «быков» и «коров» в названном числе
  «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
что и в задуманном числе
  «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,что и в задуманном числе  
''', color='magenta')

game()

while input(colored("Хотите еще партию? (введите 'да' для запуска новой игры): ", color='blue')) == 'да':
    game()

cprint('Приходите ещё!', color='grey', attrs=['underline'])
