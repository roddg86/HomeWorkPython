""" 1) В файле находится N натуральных чисел, 
записанных через пробел.
Среди чисел не хватает одного, 
чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
Пример:
3,4,5,7,8,9
Вывод:
6
"""

# file = open("Seminar/file.txt", 'r')
# li = [int(i) for i in file.read().split()]

# for i in range(1, len(li)):
#     if li[i]-1 != li[i-1]:
#         print(li[i] - 1)

""" 2) Написать программу, которая будет удалять 
все слова в которых есть "абв"

Ввод:
привет приаб приабвет
Вывод:
привет приаб """

# list = [i for i in input("Ведите строку: ").split()]
# new_list = []

# for i in list:
#     if 'абв' not in i:
#         new_list.append(i)

# print(*new_list)