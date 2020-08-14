# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint


class StatGenerate:

    def __init__(self, file_name='voyna-i-mir.txt', encoding='utf8'):
        self.stat = {}
        self.char_list = []
        self.char_stat = 0
        self.file_name = file_name
        self.encoding = encoding
        self.generate()

    def generate(self):
        with open(file=self.file_name, mode='r', encoding=self.encoding) as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
                        self.char_stat += 1
        self.char_list = list(self.stat.items())

    def print_stat(self):
        print('+---------+---------+')
        print('|  буква  | частота |')
        print('+---------+---------+')
        for char in self.char_list:
            print(f'|{char[0]:^9}|{char[1]:^9}|')
        print('+---------+---------+')
        print(f'|  итого  |{self.char_stat:^9}|')
        print('+---------+---------+')

    def print_a_z(self):
        self.char_list.sort()
        self.print_stat()

    def print_z_a(self):
        self.char_list.sort(reverse=True)
        self.print_stat()

    def print_9_0(self):
        self.char_list.sort(key=lambda i: i[1], reverse=True)
        self.print_stat()

    def print_0_9(self):
        self.char_list.sort(key=lambda i: i[1])
        self.print_stat()


war_and_peace = StatGenerate(encoding='cp1251')
war_and_peace.print_0_9()  # - по частоте по возрастанию
war_and_peace.print_9_0()  # - по частоте по убыванию
war_and_peace.print_a_z()  # - по алфавиту по возрастанию
war_and_peace.print_z_a()  # - по алфавиту по убыванию

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
