""" 1) Напишите программу, которая принимает 
на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """


# def product_kit(numberN):

#     list = []
#     factorial = 1

#     for current in range(numberN):
#         current += 1
#         factorial *= current
#         list.append(factorial)
#     return list


# numberN = int(input('Введите число: '))
# factorial = product_kit(numberN)
# print(factorial)


""" 2) Требуется найти наименьший натуральный 
делитель целого числа N, отличный от 1.

Пример:

Для n = 15: Ответ: 3
Для n = 35: Ответ: 5 """


# def smallest_divider(number):
#     denominator = 2
#     while numberN % denominator:
#         denominator += 1
#     return denominator


# numberN = int(input("Введите целое число: "))
# divider = smallest_divider(numberN)
# print(f"Делитель числа {numberN} равен: {divider}")

""" 3) Задайте список из (2*N+1) элементов, 
заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных ИНДЕКСАХ. 
Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

Ввод: 4
[-4, -3, -2, -1, 0, 1, 2, 3, 4] """


# from random import randint

# """ функция задает список элементов """


# def list_elements(numberN):
#     elements = []
#     for i in range(2 * numberN + 1):
#         elements.append(-numberN + i)
#     return elements


# """ функция заполняет список индексов """


# def list_index(number):
#     index = [randint(0, number) for _ in range(number)]
#     return index


# """ функция находит произведение элементов на указаных индексах """


# def product_of_elements(index, elements):
#     product = 1
#     for i in range(len(index)):
#         specified_index = index[i]
#         product *= elements[specified_index]
#     return product

# numberN = int(input('Введите число N: '))
# elements = list_elements(numberN)
# print(f'Список элементов {elements}')
# index = list_index(5)
# print(f'Список индексов {index}')
# product = product_of_elements(index, elements)
# print(f'Произведение {product}')

""" 4)Требуется посчитать сумму чётных чисел, 
расположенных между числами 1 и N включительно. """


# def sum_even_numbers(number):

#     list = []
#     sum = 0

#     for current in range(numberN):
#         current += 1
#         if current % 2 == 0:
#             sum += current
#         list.append(current)
#     print(list)
#     return sum


# numberN = int(input('Введите число: '))
# summa = sum_even_numbers(numberN)
# print(f'сумма {summa}')
