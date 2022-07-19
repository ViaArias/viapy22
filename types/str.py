# # Индексация в строке
# name = 'John'
# J = 0 = -4
# o = 1 = -3
# h = 2 = -2
# n = 3 = -1
# print(name)
# print(name[1])
# print(name[-1])

# str1 = 'birthday'
# print(str1[5], str1[6], str[7])

#  Срезы по индексам

# [start: end: <step>]
# str1 = 'birthday'
# print(str1[5:])
# print(str1[0:5]) 

# text = "Hello world! My name is john! I\'m not North\'s King"
# print(text[::-1])

# Конкатенация строк

# a = 'Hello'
# b = 'world'
# c = ' '
# result = a + c +b
# print(result)

# Экранирование - при помощи которого можно вставлять символы в трокые которые сложно ввести с клавиатуры.

#\n ->  перенос строки
#\t ->  горизонтальная табуляция
#
#
#

# name = 'John\nSnow'
# print(name)
# print(len(name))

# #Форматирование строк
# 1. С помощью %
# 2. С использованием.fromat()
# 3. Интерполяция строк(f-строки)

# 1. %
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print('Hello mr/mrs %s %s' %(name, last_name))

# 2. .format
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print('Hello mr/mrs {} {}' .format(name, last_name))

# 3. 
# a = input('Enter mr/mrs: ')
# name = input('Enter your name: ')
# last_name = input('Enter your last name: ')
# print(f'Hello {a} {last_name} {name}. Welcome to the party')

# print(dir(str))   