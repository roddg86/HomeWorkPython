""" 1. Пользователь вводит число,
Вам необходимо вывести число Пи
с той точностью знаков после запятой,
сколько указал пользователь(БЕЗ round()) """

# import math


# def not_round(num_pi, digit):
#     return f"{num_pi:.{digit}f}"


# number = int(input('Введите число: '))
# result = not_round(math.pi, number)
# print(result)


""" 2. Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.

N = 6 | N = 12    | 32                | 13 | 9     | 18        | 21
2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7 """

# def get_prime_factors(number):
#     factors_list = []
#     divisor = 2
#     while divisor <= number:
#         if number % divisor == 0:
#             factors_list.append(divisor)
#             number = number / divisor
#         else:
#             divisor += 1
#     return factors_list

# number = int(input('Введите натуральное число: '))
# result = get_prime_factors(number)
# print(result)

""" 3. Задайте последовательность чисел.
Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.

Ввод:
3 1 2 3

Вывод:
2 1
 """

# """ функция задает список из нескольких чисел """


# from random import randint
# def list_number(number):
#     index = [randint(1, number) for _ in range(number)]
#     return index


# """ функция сохраняет в новый список только те элементы,
# для которых ключевые значения упоминаются только один раз"""


# def unique_values(input_list):
#     result_list = []
#     for item in input_list:
#         if input_list.count(item) == 1:
#             result_list.append(item)
#     return result_list


# list = list_number(9)
# print(list)
# list_res = unique_values(list)
# print(*list_res) # выводит список с распаковаными элементами


""" 4. Задана натуральная степень k.
Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и вывести многочлен степени k.

Пример:

k = 2 => 2*x² + 4*x + 5

k = 6 => ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

         a, b, c, d, e, h - рандом """


# from random import randint
# def polynomial(extent):
#     for i in range(extent, 0, -1):
#         coefficient = randint(1, 100)
#         if coefficient == 1:
#             coefficient = ''
#         else:
#             coefficient = f'{coefficient} * x^{i} + ' if i != 1 else f'{coefficient} * x + '
#         print(coefficient, end='')

#     print(f'{randint(1, 100)}')


# extent = int(input('Введите степень k: '))
# polynomial(extent)


""" *** 5. Даны два файла,
в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.

2*x^  + 4*x      5*x^2 + 2*x
    7x^2 + 6x

2*x^6  + 4*x      5*x^2 + 2*x
    2*x^6 + 5x^2 + 6x """
