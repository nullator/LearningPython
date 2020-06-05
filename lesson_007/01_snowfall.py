# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, x=randint(50, 550), y=randint(500, 600), line_len=25):
        self.x = x
        self.y = y
        self.line_len = line_len

    def clear_previous_picture(self):
        self.draw(color=sd.background_color)

    def move(self):
        self.y = self.y - 10
        self.x = self.x + randint(-20, 20)

    def draw(self, color=sd.COLOR_WHITE):
        start_point = sd.get_point(self.x, self.y)
        end_point = sd.get_point(self.x, self.y + self.line_len)
        sd.line(start_point=start_point, end_point=end_point, color=color)
        end_point = sd.get_point(self.x, self.y - self.line_len)
        sd.line(start_point=start_point, end_point=end_point, color=color)
        end_point = sd.get_point(self.x + self.line_len, self.y)
        sd.line(start_point=start_point, end_point=end_point, color=color)
        end_point = sd.get_point(self.x - self.line_len, self.y)
        sd.line(start_point=start_point, end_point=end_point, color=color)
        end_point = sd.get_point(self.x + self.line_len * 0.7, self.y + self.line_len * 0.7)
        sd.line(start_point=start_point, end_point=end_point, color=color)
        end_point = sd.get_point(self.x + self.line_len * 0.7, self.y - self.line_len * 0.7)
        sd.line(start_point=start_point, end_point=end_point, color=color)
        end_point = sd.get_point(self.x - self.line_len * 0.7, self.y + self.line_len * 0.7)
        sd.line(start_point=start_point, end_point=end_point, color=color)
        end_point = sd.get_point(self.x - self.line_len * 0.7, self.y - self.line_len * 0.7)
        sd.line(start_point=start_point, end_point=end_point, color=color)

    def can_fall(self):
        if self.y >= self.line_len:
            return True


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


def get_flakes(count):
    flakes_result = []
    for i in range(count):
        x = randint(50, 550)
        y = randint(400, 550)
        line_len = randint(25, 35)
        flakes_result.append(Snowflake(x=x, y=y, line_len=line_len))
    return flakes_result


def append_flakes(count):
    for i in range(count):
        x = randint(50, 550)
        y = randint(400, 550)
        line_len = randint(25, 35)
        flakes.append(Snowflake(x=x, y=y, line_len=line_len))


N = 20

flakes = get_flakes(count=N)
while True:
    fallen_flakes = 0
    for flake in flakes:
        if not flake.can_fall():
            flakes.remove(flake)
            fallen_flakes += 1
        else:
            flake.clear_previous_picture()
            flake.move()
            flake.draw()
    if fallen_flakes:
        append_flakes(count=fallen_flakes)
        fallen_flakes = 0
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
