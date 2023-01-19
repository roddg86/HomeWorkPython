""" 1. Напишите программу вычисления арифметического выражения 
заданного строкой. Используйте операции +,-,/,*. 
приоритет операций стандартный.



*Пример:*

2+2 => 4;

1+2*3 => 7;

1-2*3 => -5; """

# expression = str(input('Введите арифметическое выражение: '))
# result = eval(expression)
# print(f'{expression} = {result}')

# string = '3 * 20 + 5 - 3 * 3'

# list = string.split(' ')


# def multy(kist):
#     while '*' in list:
#         ind = list.index('*')
#         res = int(list[ind - 1]) * int(list[ind + 1])
#         del list[(ind - 1): (ind + 2)]
#         list.insert(ind - 1, res)
#     print('*', list)
#     while '/' in list:
#         ind = list.index('/')
#         res = int(list[ind - 1]) / int(list[ind + 1])
#         del list[(ind - 1): (ind + 2)]
#         list.insert(ind - 1, res)
#     print('/', list)
#     while '-' in list:
#         ind = list.index('-')
#         res = int(list[ind - 1]) - int(list[ind + 1])
#         del list[(ind - 1): (ind + 2)]
#         list.insert(ind - 1, res)
#     print('-', list)
#     while '+' in list:
#         ind = list.index('+')
#         res = int(list[ind - 1]) + int(list[ind + 1])
#         del list[(ind - 1): (ind + 2)]
#         list.insert(ind - 1, res)
#     print('+', list)


# print(multy(list))
