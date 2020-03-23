# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

sd.resolution = (1200, 900)

color_table = {1: (255, 0, 0),
               2: (255, 127, 0),
               3: (255, 255, 0),
               4: (0, 255, 0),
               5: (0, 255, 255),
               6: (0, 0, 255),
               7: (255, 0, 255),
               }


def choice_color():
    i = int(input('Введиье желаемый цвет: '))
    if i < 1 or i > 7:
        print('Вы ввели некорректный цвет!')
        return choice_color()
    else:
        return color_table[i]


def figure(face, point, angle=0, length=300, color=sd.COLOR_YELLOW):
    if face < 3:
        print('Количество граней должно более 2')
        return None
    # if face > 20:
    #     print('Количество граней не должно быть более 20')
    #     return None
    start_point = point
    current_angle = angle
    current_length = (length * 5) / face
    for n in range(face-1):
        start_point = sd.vector(start=start_point, angle=current_angle, length=current_length, width=2, color=color)
        current_angle = current_angle + 360/face
    sd.line(start_point=start_point, end_point=point, width=2, color=color)


print('Возможные цвета: \n',
    '1: RED \n',
    '2: ORANGE \n',
    '3: YELLOW \n',
    '4: GREEN \n',
    '5: CYAN \n',
    '6: BLUE \n',
    '7: PURPLE',
    )

line_color = choice_color()

point_0 = sd.get_point(200, 150)
figure(face=3, point=point_0, angle=30, length=150, color=line_color)

point_0 = sd.get_point(800, 150)
figure(face=4, point=point_0, angle=30, length=150, color=line_color)

point_0 = sd.get_point(200, 500)
figure(face=5, point=point_0, angle=30, length=150, color=line_color)

point_0 = sd.get_point(800, 500)
figure(face=6, point=point_0, angle=30, length=150, color=line_color)

sd.pause()
