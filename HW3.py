""" 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

""" функция задает список из нескольких чисел """


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


""" 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

""" 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

""" 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

""" bin(45) """

# def to_binary(n):
#     result = ''
#     while n > 0:
#         result = str(n % 2) + result
#         n = n // 2
#     return result


# n = int(input('Введите целое число '))
# print(to_binary(n))

""" 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """
