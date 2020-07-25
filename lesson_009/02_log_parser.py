# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class LogParser:

    def __init__(self, file_name="events.txt", encoding='utf8', interval='minute'):
        self.counter = 0
        self.last_time = None
        self.now_time = None
        self.end_char = None
        self.file_name = file_name
        self.out_file_name = None
        self.out_file = None
        self.encoding = encoding
        self.__set_interval(interval)

    def __set_interval(self, interval):
        if interval == 'minute':
            self.end_char = 17
            self.out_file_name = 'out_minute.txt'
        elif interval == 'hour':
            self.end_char = 14
            self.out_file_name = 'out_hour.txt'
        elif interval == 'day':
            self.end_char = 11
            self.out_file_name = 'out_day.txt'
        elif interval == 'month':
            self.end_char = 8
            self.out_file_name = 'out_month.txt'
        elif interval == 'year':
            self.end_char = 5
            self.out_file_name = 'out_year.txt'

    def parse(self, interval=None):
        if interval is not None:
            self.__set_interval(interval)
        self.out_file = open(self.out_file_name, 'w', encoding=self.encoding)
        self.counter = 0
        with open(file="events.txt", mode='r') as file:
            self.last_time = file.readline(17)[1:self.end_char]
        with open(file="events.txt", mode='r') as file:
            for line in file:
                event = line[29:]
                self.now_time = line[1:self.end_char]
                if self.now_time != self.last_time:
                    self.__print_interval_statistics__()
                    self.counter = 0
                    self.last_time = self.now_time
                if event[0:3] == "NOK":
                    self.counter += 1
            self.__print_last_line__()
            self.out_file.close()

    def __print_interval_statistics__(self):
        if self.end_char == 14:
            current_hour = int(self.last_time[11:14])
            if 9 >= current_hour >= 0:
                output = f'[{self.last_time}:00 - 0{current_hour}:59] {self.counter}'
                print(output)
                self.out_file.write(output+'\n')
            else:
                output = f'[{self.last_time}:00 - {current_hour}:59] {self.counter}'
                print(output)
                self.out_file.write(output + '\n')
        else:
            output = f'[{self.last_time}] {self.counter}'
            print(output)
            self.out_file.write(output + '\n')

    def __print_last_line__(self):
        if self.end_char == 14:
            current_hour = int(self.now_time[11:14])
            if 9 >= current_hour >= 0:
                output = f'[{self.now_time}:00 - 0{current_hour}:59] {self.counter}'
                print(output)
                self.out_file.write(output + '\n')
            else:
                output = f'[{self.now_time}:00 - {current_hour}:59] {self.counter}'
                print(output)
                self.out_file.write(output + '\n')
        else:
            output = f'[{self.now_time}] {self.counter}'
            print(output)
            self.out_file.write(output + '\n')


test = LogParser()

print('По умолчанию группировка по минутам:')
test.parse()
print('')

print("Группировка по часам:")
test.parse('hour')
print('')

print("Группировка по дням:")
test.parse('day')
print('')

print("Группировка по месяцам:")
test.parse('month')
print('')

print("Группировка по годам:")
test.parse('year')


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
