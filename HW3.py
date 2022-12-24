""" 1. Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

# """ функция задает список из нескольких чисел """


# from random import randint
# def list_number(number):
#     index = [randint(1, number) for _ in range(number)]
#     return index


# """ функция находит сумму чисел на нечетных позициях """


# def sum_odd(list):
#     sum = 0
#     for item in range(1, len(list), 2):
#         sum += list[item]
#     return sum


# lst_number = list_number(6)
# print(f'Список чисел {lst_number}')
# result = sum_odd(lst_number)
# print(f'Сумма чисел на нечетных позициях {result}')


""" 2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """


# from random import randint

# def gen_list(number):
#     list = []
#     for i in range(number):
#         list.append(randint(1, 9))
#     return list

# def product_pairs(list):
#     list2 = []
#     i = 0
#     number = len(list)
#     while i < len(list)//2 + len(list) % 2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1
#     return list2

# number = int(input('Введите размер списка: '))
# list = gen_list(number)
# print(list)
# print(product_pairs(list))


""" 3. Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением
дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """


# from random import randint, uniform
# def generate_list(number):

#     my_list = []

#     for _ in range(number):
#         fract_part = randint(1, 2)
#         my_list.append(round(uniform(1, 10), fract_part))
#     return my_list


# def difference(my_list):
#     min = 1
#     max = 0
#     max_min = 0

#     for i in my_list:
#         if (i - int(i)) <= min:
#             min = i - int(i)
#         if (i - int(i)) >= max:
#             max = i - int(i)
#     max_min = round((max - min), 2)
#     return max_min


# number = int(input('Введите число: '))
# my_list = generate_list(number)
# #my_list = [1.1, 1.2, 3.1, 10.01]
# print(f'Исходный список: {my_list}')
# print(difference(my_list))


""" 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

""" bin(45) """

# def to_binary(number):
#     result = ''
#     while number > 0:
#         result = str(number % 2) + result
#         number = number // 2
#     return result


# n = int(input('Введите целое число '))
# print(to_binary(n))

""" 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """


# def fibonacci(number):

#     list = [0, 1]
#     for i in range(2, number + 1):
#         list.append(list[-1] + list[-2])
#     for i in range(number):
#         list = [list[1] - list[0]] + list
#     return list


# number = int(input("Введите  число:\n"))
# print(f'для k = {number} список будет выглядеть так: {fibonacci(number)}')
