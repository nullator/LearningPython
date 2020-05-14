from random import randint

_number = []


def generate_number():
    global _number
    _number = []
    all_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    _number.append(all_number.pop(randint(0, len(all_number) - 1)))
    all_number.append(0)
    for i in range(3):
        _number.append(all_number.pop(randint(0, len(all_number) - 1)))
    # print(_number)


def check_number(user_number):
    # Проверка правила о том, что загаданное число должно состоять из 4 цифр
    if int(user_number) < 1000 or int(user_number) > 9999:
        return None

    # Проверка правила о том, что все цифры в загаданном числе должны быть разные
    check_rule = set()
    for i in range(4):
        check_rule.add(user_number[i])
    if len(check_rule) < 4:
        return None

    # Подсчёт быков, остальных животных отправляем в новый список
    bulls = 0
    new_number = []
    new_user_number = []
    for i in range(4):
        if _number[i] == int(user_number[i]):
            bulls += 1
        else:
            new_number.append(_number[i])
            new_user_number.append(int(user_number[i]))

    # Подсчёт коров
    cows = 0
    for i in range(0, len(new_number)):
        if new_user_number[i] in new_number:
            cows += 1

    # print('Быков: ', bulls, ', коров: ', cows)
    return {'bulls': bulls, 'cows': cows}
