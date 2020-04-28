# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 900)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

point_0 = sd.get_point(300, 250)


def figure(face, point, angle=0, length=150):
    if face < 3:
        print('Количество граней должно более 2')
        return None
    if face > 20:
        print('Количество граней должно не больше 20') # Если много граней - некрасиво замыкается
        return None
    start_point = point
    current_angle = angle
    current_length = (length * 5) / face # Для того чтобы при большом количестве граней рисовало красиво
    for n in range(face-1):
        # Цикл для рисования всех граней, кроме последней
        # На каждой итерации меняются начальние точки и угол на новые
        start_point = sd.vector(start=start_point, angle=current_angle, length=current_length, width=2)
        current_angle = current_angle + 360/face
    sd.line(start_point=start_point, end_point=point, width=2) # Рисование последней грани для замыкания с начальной точкой


face = int(input('Введите количество граней: '))
figure(face, point_0, 0, 300)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()