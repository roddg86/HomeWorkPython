""" 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

*Примеры:*

- 5, 25 -> да
- 4, 16 -> да
- 25, 5 -> да
- 8,9 -> нет """

""" a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

if a == b**2 or b == a**2:
    print('ДА')
else:
    print("НЕТ") """

""" 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

Примеры:

- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90 """

""" a, b, c, d, e = int(input("Введите пять чисел ")), int(
    input()), int(input()), int(input()), int(input())

print(f'Максимальное число: {max(a,b,c,d,e)}') """

""" 3. С клавиатуры введено трехзначное число найти сумму его цифр """

""" a = int(input("Введите терхзначное число "))

print((a // 100) + (a % 100 // 10) + (a % 10)) """

""" 4. Даны два числа проверить что первое делиться на второе """