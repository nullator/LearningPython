# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = (1200, 900)


def figure(face, point, angle=0, length=300, color=sd.COLOR_YELLOW):
    if face < 3:
        print('Количество граней должно более 2')
        return None
    # if face > 20:
    #     print('Количество граней не должно быть более 20')
    #     return None
    start_point = point
    current_angle = angle
    current_length = (length * 4) / face
    for n in range(face-1):
        start_point = sd.vector(start=start_point, angle=current_angle, length=current_length, width=2, color=color)
        current_angle = current_angle + 360/face
    sd.line(start_point=start_point, end_point=point, width=2, color=color)


print('Возможные фигуры: \n',
    '0: треугольник \n',
    '1: квадрат \n',
    '2: пятиугольник \n',
    '3: шестиугольник',
    )

point_0 = sd.get_point(400, 200)
n = 0
while n < 3 or n > 6:
    n = int(input('Введите желаемую фигуру: ')) + 3
    if 3 <= n <= 6:
        break
    print('Вы ввели некорректную фигуру!')
figure(face=n, point=point_0)

sd.pause()
