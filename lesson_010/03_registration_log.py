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
	Считывает строку, проверяет значения. При выявлении ошибки вызывает исключение.
	В случае если ошибок нет - возвращает список со значениями
	'''
	name, email, age = line.split(" ")
	if check_name(name) and check_email(email) and check_age(age):
		return [name, email, age]
	
	
def check_name(name: str):
	'''
	Проверяет имя. Должно содержать только буквы, если содержит цифры - вызывает ощибку NotNameError
	'''
	if not name.isalpha():
		raise NotNameError(f'Некорректное имя - {name}')
	else: 
		return True
	

def check_email(email: str):
	'''
	Проверяет адрес почты. Если в адресе нет символов "@" и "." - вызывает ошибку NotEmailError
	'''
	if '@' not in email or '.' not in email:
		raise NotEmailError(f'Указана несуществующая электронная почта - {email}')
	else:
		return True
		
		
def check_age(age: str):
	'''
	Проверяет возраст. По условиям задачи возраст должен быть в промежутке от 10 до 99.
	Если возраст не соответствует условиям - вызывает ошибку ValueError.
	Если возраст не является числом - вызывает ошибку ValueError.
	'''
	if re.search('\n', age) is not None:
		age = age[:-1]
	if age.isdigit():
		if int(age) < 10 or int(age) > 99:
			raise ValueError(f'Возраст ({age}) выходит за пределы 10 - 99 лет')
		else:
			return True
	else:
		raise ValueError(f"Указано значение возраста ({age}). Значение возраста должно содержать цифры")
	

registration_good_log = []
registration_bad_log = []
with open('registrations.txt', 'r', encoding='utf8') as file:
	for line in file:
		try:
			check_line(line)
			registration_good_log.append(line)
		except ValueError as exc:
			if 'unpack' in exc.args[0]:
				registration_bad_log.append(f'Не хватает операндов в строке \"{line}\"')
				# print(f'Не хватает операндов в строке \"{line}\"')
			else:
				registration_bad_log.append(exc.args[0] + f' в строке \"{line}\"')
				# print(exc.args[0] + f' в строке \"{line}\"')
		except NotEmailError as exc:
			registration_bad_log.append(exc.args[0] + f' в строке \"{line}\"')
			# print(exc.args[0] + f' в строке \"{line}\"')
		except NotNameError as exc:
			registration_bad_log.append(exc.args[0] + f' в строке \"{line}\"')
			# print(exc.args[0] + f' в строке \"{line}\"')

with open('registrations_good.log', 'w', encoding='utf8') as good_log_file:
	good_log_file.writelines(registration_good_log)

with open('registrations_bad.log', 'w', encoding='utf8') as bad_log_file:
	bad_log_file.writelines(registration_bad_log)

print(f'Всего обработано {len(registration_good_log)+len(registration_bad_log)} записей')
print(f'Корректные записи в количестве {len(registration_good_log)} записаны в файл registrations_good.log')
print(f'Некорректные записи в количестве {len(registration_bad_log)} записаны в файл registrations_bad.log')