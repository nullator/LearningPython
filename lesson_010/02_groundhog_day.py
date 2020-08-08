# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint


ENLIGHTENMENT_CARMA_LEVEL = 777

class IamGodError(Exception):
	pass
	
class DrunkError(Exception):
	pass
	
class CarCrashError(Exception):
	pass

class GluttonyError(Exception):
	pass

class DepressionError(Exception):
	pass

class SuicideError(Exception):
	pass

exceptions = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]

def one_day():
	if randint(1, 13) == 13:
		raise exceptions[randint(0, 5)]
	return randint(1, 7)
	
carma = 0
with open('log.txt', 'w') as file:
	while carma < ENLIGHTENMENT_CARMA_LEVEL:
		try:
			carma += one_day()		
		except IamGodError:
			file.write(f'I am God error, my carma = {carma}\n')
		except DrunkError:
			file.write(f'Drunk error, my carma = {carma}\n')
		except CarCrashError:
			file.write(f'Car crash error, my carma = {carma}\n')
		except GluttonyError:
			file.write(f'Gluttony error, my carma = {carma}\n')
		except DepressionError:
			file.write(f'Depression error, my carma = {carma}\n')
		except SuicideError:
			file.write(f'Suicide error, my carma = {carma}\n')
		except:
			file.write(f'Неизвестная ошибка, my carma = {carma}\n')
			
print(carma)	
	

# https://goo.gl/JnsDqu
