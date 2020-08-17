# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.prime_numbers = []
        self.i = 0
        self.number = 2

    def __iter__(self):
        self.i = 0
        return self

    def prime_numbers_generator(self):
        for number in range(2, self.n + 1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.prime_numbers.append(number)
                self.number = number
                yield self.number

    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return next(self.prime_numbers_generator())
        else:
            raise StopIteration


# prime_number_iterator = PrimeNumbers(n=100)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# for number in prime_numbers_generator(n=100):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def happy_number(number: int):
    """
    Проверка является ли число счястливым
    """
    str_number = str(number)
    number_len = len(str_number)
    n = number_len // 2
    numbers = tuple(map(int, str_number))

    # Проверка является ли количество цифр в числе четным
    if (number_len % 2) == 0:
        is_even = True
    else:
        is_even = False

    left_side = sum(numbers[:n])
    if is_even:
        right_side = sum(numbers[n:])
    else:
        right_side = sum(numbers[n+1:])  # Если количество цифр в числе нечётное, среднюю цифру не учитываем

    if left_side == right_side:
        print('True')
    else:
        print('False')

    return left_side == right_side


def palindrome_number(number: int):
    """
    Проверка является ли число палиндромом
    """
    str_number = str(number)
    list_number = list(str_number)
    list_number.reverse()
    reverse_number = "".join(list_number)

    if str_number == reverse_number:
        print('True')
    else:
        print("False")

    return str_number == reverse_number


happy_number(92083)
palindrome_number(92083)
palindrome_number(101)