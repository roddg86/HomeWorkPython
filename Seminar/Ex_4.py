""" 1. Задайте строку из набора чисел.
Напишите программу, которая покажет большее и меньшее число.
В качестве символа-разделителя используйте пробел.Без min и max """

# str = input('Введите строку из чисел: ').split(" ")
# print(str)
# max = int(str[0])
# min = int(str[0])

# for i in str:
#     if int(i) > max:
#         max = int(i)
#     if int(i) < min:
#         min = int(i)
# print(max, min)


""" 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0
с помощью математических формул нахождения корней квадратного уравнения """

# a, b, c = int(input('Введите A, B, C: \n')), int(input()), int(input())
# print(a, b, c)

# d = b**2 - 4 * a * c

# if d >= 0:
#     x1 = (-b + d**0.5)/(2*a)
#     x2 = (-b - d**0.5)/(2*a)
#     print(round(x1, 3), round(x2, 3))
# elif d == 0:
#     x = -b / 2
#     print(round(x, 3))
# else:
#     print('Действительных корней нет ')

""" 3. Задайте два числа.
Напишите программу, которая найдёт НОК (наименьшее общее кратное)
этих двух чисел. """

# n1, n2 = int(input('Введите числа: \n')), int(input())
# if n1 == 0 or n2 == 0:
#     print('not')
# else:
#     for nok in range(max(n1, n2), n1*n2+1):
#         if nok % n1 == 0 and nok % n2 == 0:
#             break
#     print(nok)
