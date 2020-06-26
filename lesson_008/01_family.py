# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.pet_food = 50
        self.dirt = 0

    def __str__(self):
        return f"В доме {self.money} денег, {self.food} еды, {self.pet_food} корма и {self.dirt} грязи"


class Man:
    total_coat = 0
    total_money = 0
    total_eat = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = None

    def __str__(self):
        return f"{self.name}: сытость = {self.fullness}, счастье = {self.happy}"

    def eat(self):
        if self.house.food > 0:
            if self.house.food >= 30:
                self.fullness += 30
                self.house.food -= 30
                Man.total_eat += 30
                print(f'{self.name} поел')
            else:
                self.fullness += self.house.food
                Man.total_eat += self.house.food
                self.house.food = 0
                print(f'{self.name} поел, еды больше нет')
        else:
            print(f'{self.name} не смог поесть, нет еды')

    def act(self):
        if self.fullness <= 0 or self.happy < 10:
            print(f'{self.name} умер')
            return 'Dead'
        if self.house.dirt >= 90:
            self.happy -= 10
            print(f'{self.name} несчастлив от грязи дома')
        self.house.dirt += 5


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 5)
        if self.fullness <= 20:
            self.eat()
        elif self.house.money <= 100:
            self.work()
        elif dice == 1:
            self.eat()
        elif 2 <= dice <= 4:
            self.work()
        elif dice == 5:
            self.gaming()

    def eat(self):
        super().eat()

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        Man.total_money += 150
        print(f'{self.name} сходил на работу')

    def gaming(self):
        self.happy += 20
        self.fullness -= 10
        print(f'{self.name} играл')


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 8)
        if self.fullness <= 20:
            self.eat()
        elif self.house.dirt > 100:
            self.clean_house()
        elif dice <= 1:
            self.eat()
        elif 2 <= dice <= 5:
            self.shopping()
        elif 6 <= dice <= 7:
            self.clean_house()
        elif dice == 8:
            self.buy_fur_coat()

    def eat(self):
        super().eat()

    def shopping(self):
        if self.house.money >= 150:
            self.house.food += 150
            self.house.pet_food += 00
            self.house.money -= 150
            self.fullness -= 10
            print(f'{self.name} купила еды')
        elif self.house.money > 0:
            self.house.food += self.house.money
            self.house.money = 0
            self.fullness -= 10
            print(f'{self.name} купила еды на все деньги')
        else:
            self.fullness -= 10
            print(f'{self.name} хотела купить еды, но дене нет')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.happy += 60
            self.fullness -= 10
            Man.total_coat += 1
            print(f'{self.name} купила шубу!')
        else:
            print(f'{self.name} хочет шубу')

    def clean_house(self):
        if self.house.dirt <= 100:
            self.house.dirt = 0
            self.fullness -= 10
            print(f'{self.name} убралась дома до идеальной чистоты')
        else:
            self.house.dirt -= 100
            self.fullness -= 10
            print(f'{self.name} убралась дома')


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act() is not "Dead":
            dice = randint(1, 2)
            if self.fullness <= 20:
                self.eat()
            elif dice == 1:
                self.eat()
            else:
                self.sleep()
            self.happy = 100
        else:
            print(f'{self.name} мёртв')

    def eat(self):
        if self.house.food > 0:
            if self.house.food >= 10:
                self.fullness += 10
                Man.total_eat += 10
                self.house.food -= 10
                print(f'{self.name} поел')
            else:
                self.fullness += self.house.food
                Man.total_eat += self.house.food
                self.house.food = 0
                print(f'{self.name} доел всю еду в доме')
        else:
            print(f'{self.name} не смог поесть, нет еды')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} спит')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')

serge.house = home
masha.house = home
kolya.house = home

for day in range(365):
    cprint('================== День {} =================='.format(day+1), color='red')
    serge.act()
    masha.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='cyan')

print('')
cprint(f'Всего заработано {Man.total_money} денег, съедено {Man.total_eat} еды, куплено {Man.total_coat} шуб', color='red')

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass



######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

