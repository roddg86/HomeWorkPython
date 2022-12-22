# list = [1, "stroka", 1]
# list.append(13)
# list[2]

# kortez = (1, "stroka", 3)
# kortez = (1,"stroka",3)
# print(kortez[0])
# print(kortez[1])

# a,b,c = (1,"stroka",3)

#slovar = {1: "one", "st": "two"}
# slovar[5] = [1,2,3]
# slovar[5].append(4)
# for item in slovar:
#     print(item, slovar[item])

# mnoj = set()
# for i in range(100):
#     mnoj.add(i)

# mnoj.add(1)
# mnoj.add(2)
# mnoj.add(1)
# print(mnoj)

""" 1.Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число. """

number = int(input('Введите число '))
list = ["qwe", "asd", "zxc", "qwe", "5","ertqwe"]

if str(number) in list:
    print(f'в списке есть число {number}')
else:
    print('числа нет')

""" 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

*Пример:*

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1 """

# list = ["qwe", "asd", "zxc", "qwe", 5, "ertqwe"]
# str = input('Введите строку ')
# count = 0

# for i in range(len(list)):
#     if list[i] == str:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# if count < 2:
#     print('строки нет')