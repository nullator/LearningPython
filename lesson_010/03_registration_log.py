# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import re


class NotNameError(Exception):
	pass
	
	
class NotEmailError(Exception):
	pass
	

def check_line(line):
	'''
	Считывает строку, проверяет значения. При выявленииошибки вызывает исключение. В случае если ошибок нет - возвращает список со значениями
	'''
	name, email, age = line.split(" ")
	if check_name(name) and check_email(email) and check_age(age):
		return [name, email, age]
	
	
def check_name(name):
	if re.search('\d+', name) is not None:
		raise NotNameError(f'Указано имя - {name}. Имя должно содержать только буквы без цифр')
	else: 
		return True
	

def check_email(email):
	if re.search('@', email) is None or re.search('.', email) is None:
		raise NotEmailError(f'Указана несуществующая электронная почта - {email}')
	else:
		return True
		
		
def check_age(age):
	if age.isdigit():
		if int(age) < 10 or int(age) > 99:
			raise ValueError(f'Некорректное значение возраста ({age}). Возраст должен быть в промежутке 10 - 99')
		else:
			return True
	else:
		raise ValueError(f"Указано значение возраста - {age}. Значение возраста должно содержать цифры")
	

registration_good_log = []
registrarion_bad_log = []						
with open('registrations.txt', 'r') as file:
	for line in file:
		line = line[:-1]	
		print(check_line(line))
		