""" Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
оставшихся чисел в одну строчку через пробел.
[1,2,3,4,22,234,24] ----> [22, 24]
 """
# list_num = list(map(int, input('Введте числа через пробел: ').split()))
# print(*list(filter(lambda x: 9 < x < 100, list_num)))

""" Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
[12,'sadf',5643] ---> ['sadf'] ,[12,5643]
 """

# list_init = [12, 'sadf', 5643]
# print(f"Исходный список: {list_init}\nРазделённые списки: {list(filter(lambda x: not type(x) == int, list_init))}, {list(filter(lambda x: type(x) == int, list_init))}")

""" Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """

# print(sum(map(int, list(map(int, list(filter(lambda x: x.isdigit(), input('Введите любое число: '))))))))
