""" 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

*Примеры:*

- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет """

""" a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
 """
""" if a == b**2 or b == a**2:
    print('ДА')
else:
    print("НЕТ") """

# print(a ** 2 == b or b ** 2 == a) # второе решение

""" 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

Примеры:

- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90 """

""" a, b, c, d, e = int(input("Введите пять чисел ")), int(
    input()), int(input()), int(input()), int(input())

print(f'Максимальное число: {max(a,b,c,d,e)}') """

""" list = []
for i in range(5):
    list.append(int(input(f'Введите {i + 1} число: ')))

max = list[0]
for i in list:
    if i >= max:
        max = i
print(f'Максимальное число  {max}')
 """

""" def find_max(lst_nums):
    max_num = lst_nums[0]

    for number in lst_nums:
        if number > max_num:
            max_num = number
        
    return max_num

lst_in = []

number_els = int(input('Введите количество элементов: '))

for i in range(number_els):
    lst_in.append(int(input(f'Введите {i+1} элемент: ')))

print(find_max(lst_in))
 """
""" list = []

for i in range(0,5):
    list.append(int(input(f'Введите {i + 1} элемент: ')))

print(max(list)) """

""" 3. С клавиатуры введено трехзначное число найти сумму его цифр """

""" a = int(input("Введите терхзначное число "))

print((a // 100) + (a % 100 // 10) + (a % 10)) """

""" 4. Даны два числа проверить что первое делиться на второе """

""" a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

if b != 0:
    if a % b == 0:
        print('Да')
    else:
        print('НЕТ')
else:
    print('На ноль делить нельзя') """

""" 5. Напишите программу, которая будет на вход принимать 
число N и выводить числа от -N до N

*Примеры:*

- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
 """
""" 
a = abs(int(input("Введите число N ")))

# for i in range(-a, a+1): print(i, end=' ')

# второе решение
lst_nums = list(range(-a, a + 1)) 
print(*lst_nums, sep=', ') """

""" 6. Напишите программу, которая будет принимать на вход 
дробь и показывать первую цифру дробной части числа.

*Примеры:*

- 6,78 -> 7
- 5 -> нет
- 0,34 -> 3     """

""" from math import *

a = float(input("Введите число: "))

if a - floor(a) != 0:
    print(floor(a*10) % 10)
else:
    print('Дробной части нет!!!!!')
 """

""" 
# через приведение типа

from math import *

a = float(input("Введите число: "))

if a - int(a) != 0:
    print(int(a*10) % 10)
else:
    print('Дробной части нет!!!!!')
 """

# еще одно решение
number = float(input('Введите число: '))

if number % 1 == 0:
    print('Нет')
else:
    digit = number * 10 % 10
    print(int(digit))
