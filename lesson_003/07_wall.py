# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


def brick(x, y):
    start_point_1 = simple_draw.get_point(x, y)
    start_point_2 = simple_draw.get_point(x + 100, y + 50)
    end_point_1 = simple_draw.get_point(x + 100, y)
    end_point_2 = simple_draw.get_point(x, y + 50)
    simple_draw.line(start_point_1, end_point_1, simple_draw.COLOR_ORANGE, 2)
    simple_draw.line(start_point_1, end_point_2, simple_draw.COLOR_ORANGE, 2)
    simple_draw.line(start_point_2, end_point_1, simple_draw.COLOR_ORANGE, 2)
    simple_draw.line(start_point_2, end_point_2, simple_draw.COLOR_ORANGE, 2)


x, y = -50, -50
for i in range(12):
    y += 50
    if i % 2 == 0:
        x = -100
    else:
        x = -150
    for j in range(7):
        x += 100
        brick(x, y)


simple_draw.pause()
