# Тип данных int()

# # +
# a = 10
# b = 5
# result = a + b
# print(result)
# print (a + 100)

# a = 10
# b = 60
# c = 100
# d = 1000000
# e = 50

# print(a + b + c + d + e)

#/ and //

# num1 = 25
# num2 = 12

# print(num1 / num2)
# print(num1 // num2)

# % - остаток от деления

# a = 5
# b = 2

# print(a%b)

#** -> Возведение в степень

# 5**4 = 625

# a = 5
# b = 2
# print(pow(a, b))

# round() - округление числа с плавабщей точкой

# a = 5.728232
# result = round(a)
# print(result)

# abs() - абсолютное значение(модуль) -> abs(-5) => 5

# a = abs(-16)
# print(a)

#divmod(a, b) -> выводит два числа, первое число результат целочисленного делени (//) a на b. Второе число - модульное деление (%) a на b.

# a = 5
# b = 2
# result = divmod(a, b)
# print(result)

# import math

# a = 5

# print(math.sqrt(a))

# chisloPi = math.pi
# print(chisloPi)

# множесвенное присваивание
# оператор присваивания (=)

# a, b, c = c, a, b

# print(a)
# print(b)
# print(c)

# from math import pi

# r = 10
# result_P = 2 * r * pi
# result_S = pi * (r ** 2)

# print("Периметр окружности: ", result_P)
# print("Площадь окружности: ", result_S)



# # a = 10
# # b = 5
# # print(pow(a, b))
# # print(pow(b, a))

# # num = 6
# # num = 'string'
# # print(num)
# # print(type(num))

# # # from turtle import st


# # str1 = 'Hello world'
# # # num = 5
# # # print(str1 + str(num))


# # var = input('type smth: ')
# # print(var)
# # print(type(var))

# num1 = int(input('type the number: '))
# num2 = int(input('input the degree: '))
# print(num1 ** num2)
# print(pow(num1,num2))



from ntpath import join
from random import randint
name = input('Name: ')
last_name = input('Last_name: ')
num = str(randint(111111, 999999))
print(name + last_name + str(num))
# print(num)
num = set(num)
# print(num)
num = ''.join(num)
# print(num)
print(name + last_name + num)