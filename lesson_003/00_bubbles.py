# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(600, 300)
# radius = 100
# for _ in range(3):
#     sd.circle(center_position=point, radius=radius, width=2)
#     radius += 10


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def my_bubble(my_point, step=5, radius=50, my_color=sd.COLOR_DARK_YELLOW):
    for _ in range(3):
        sd.circle(center_position=my_point, radius=radius, width=1, color=my_color)
        radius += step


# Нарисовать 10 пузырьков в ряд
# x, y = 150, 150
# point = sd.get_point(x, y)
# for _ in range(10):
#     my_bubble(point)
#     x += 75
#     point = sd.get_point(x, y)


# Нарисовать три ряда по 10 пузырьков
# y = 75
# for i in range(3):
#     y += 75
#     x = 150
#     for j in range(10):
#         point = sd.get_point(x, y)
#         my_bubble(point)
#         x += 75


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.get_point(random.randint(0, 1200), random.randint(0, 600))
    color = sd.random_color()
    my_bubble(my_point=point, step=random.randint(2, 5), my_color=color)

sd.pause()
