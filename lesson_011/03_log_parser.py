# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def log_parser_generator(file_name="events.txt"):
    """
    Функция-генератор для парсинга log файла.
    Читает исходный файл (по умолчанию events.txt) и выдает число событий NOK за каждую минуту
    в формате <время> <число повторений>.
    Пример использования:
    for group_time, event_count in (log_parser_generator()):
        print(f'[{group_time}] {event_count}')
    :param file_name: Наименование TXT файла с логом
    :return: возвращает в текстовом виде минуту и количество событий 'NOK' за эту минуту
    """
    event_count = 0
    # чтение первой строки для инициализации переменной
    with open(file=file_name, mode='r') as file:
        last_time = file.readline(17)[1:17]
    with open(file=file_name, mode='r') as file:
        for line in file:
            event = line[29:]
            new_time = line[1:17]
            if new_time != last_time:
                yield last_time, event_count
                event_count = 0
                last_time = new_time
            if event[0:3] == "NOK":
                event_count += 1
        # вывод данных с учетом последней строки log файла
        yield new_time, event_count


for group_time, event_count in (log_parser_generator()):
    print(f'[{group_time}] {event_count}')