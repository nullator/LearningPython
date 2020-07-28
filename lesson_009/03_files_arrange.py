# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class FileArrange:

    def __init__(self, source, destination):
        self.root_path = os.path.dirname(__file__)
        self.source_dir = os.path.normpath(os.path.join(self.root_path, source))
        self.destination_dir = os.path.normpath(os.path.join(self.root_path, destination))
        self.files_attr = {}

    def prepare(self):
        '''Сканирует исходную деррикторию, записывает путь к файлу, год и месяц создания всех файлов в словарь'''
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                full_file_name = os.path.normpath(os.path.join(root, file))
                full_time = time.gmtime(os.path.getmtime(full_file_name))
                year = str(full_time[0])
                if full_time[1] < 10:
                    month = '0' + str(full_time[1])
                else:
                    month = str(full_time[1])
                self.files_attr[full_file_name] = year, month

    def copy_files(self):
        '''Сохдаёт пустые папки назначения, копирует в них файлы'''
        for images, attr in self.files_attr.items():
            destination = os.path.normpath(os.path.join(self.destination_dir, attr[0], attr[1]))
            os.makedirs(destination, exist_ok=True)
            shutil.copy2(src=images, dst=destination)


Files = FileArrange(source='icons', destination='icons_by_year')
Files.prepare()
Files.copy_files()



# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
