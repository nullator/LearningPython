## Imports
from pprint import pprint
from random import randint
from zipfile import ZipFile

## Settings
file_name = 'voyna-i-mir.txt.zip'
length_of_generated_text_in_char = 1000
number_of_char = 10


def open_files_from_zip(file_name='input.zip'):
    zip_file = ZipFile(file=file_name, mode='r')
    file_list = []
    for filename in zip_file.namelist():
        zip_file.extract(filename)
        file_list.append(filename)
    return file_list


stat = {}
totals = {}
stat_for_generate = {}
sequence = ' ' * number_of_char

file_list = open_files_from_zip(file_name)
with open(file_list[0], mode='r', encoding='cp1251') as file:
    for line in file:
        for char in line[:-1]:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char


for sequence, char_stats in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []
    for char, char_count in char_stats.items():
        totals[sequence] += char_count
        stat_for_generate[sequence].append([char_count, char])
    stat_for_generate[sequence].sort(reverse=True)


sequence = ' ' * number_of_char
count_of_characters_generated = 0
count_of_space = 0
while count_of_characters_generated <= length_of_generated_text_in_char:
    char_stats = stat_for_generate[sequence]
    total_for_char = totals[sequence]
    dice = randint(1, total_for_char)
    pos = 0
    for count, char in char_stats:
        pos += count
        if pos >= dice:
            print(char, end='')
            if char == " ":
                count_of_space += 1
            if count_of_space == 10:
                print('')
                count_of_space = 0
            count_of_characters_generated += 1
            sequence = sequence[1:] + char
            break





