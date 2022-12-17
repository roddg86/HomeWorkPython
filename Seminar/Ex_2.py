""" 1) Напишите программу, которая принимает на вход число N
 и выдаёт последовательность размера N 
 из чередующихся по знаку степеней тройки.

*Пример:*
- Для N = 5: 1, -3, 9, -27, 81 """

""" n = int(input("Введите число "))
for i in range(n):
    if i % 2 == 1:
        print(-3**i, end = ' ')
    else:
        print(3**i, end = ' ')    
 """

""" n = int(input("Введите число "))

lst_pow = []
for i in range(n):
    lst_pow.append((-3) ** i)

print(*lst_pow, sep=' | ')
 """

""" 2) Напишите программу, в которой пользователь будет 
задавать две строки, одна из них - буква, а вторая фраза/слово,
программа должна посчитать сколько раз буква встретилась 
буква во второй строке. (Не используя встроенные функции) """

""" phrase = input('Введите фразу: ')
letter = input('Введите букву: ')

count = 0
for i in phrase:
    if i == letter: 
        count += 1

print(f'{letter} содержится в строке "{phrase}" {count} раз')
 """

""" 3) Петя и катя - брат и сестра. 
Петя - студент, а Катя - школьница. 
Петя помогает Кате по математике.
Он задумывает два натуральных числа, а Катя должна их отгадать
Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P
Помогите Кате отгадать задуманные Петей числа.

*Пример*
Ввод: 4 4
Вывод: 2 2

*Пример*
Ввод: 5 6
Вывод: 2 3 """

""" S = int(input('S = '))
P = int(input('P = '))

bool = True
for a in range(S):
    for b in range(S):
        if a + b == S and a * b == P:
            print(a, b)
            bool = False
            break
    if bool == False:
        break    
 """

# summation, composition = map(int, input().split())
# limit = summation

# if summation < composition:
#     limit = composition
# for i in range(0, limit + 1):
#     if(summation - i) * i == composition:
#         print(summation - i, i)
#         break

# a = int(input('S = '))
# b = int(input('P = '))

# x = 0
# y = 1

# while (x + y != a) or (x * y != b):
#     y += 1
#     x = b // y

# print(f'x = {x}, y = {y}')

""" 4) Дан список из 5 неповторяющихся ростов учеников, 
дан еще ученик, куда вставить ученика в штрнеге по росту.
Список отсортирован по уменьшению. """

# amount = 5
# list = []

# for i in range(amount):
#     list.append(int(input(f'Рост {i + 1}ого ученика: ')))

# height = int(input('Рост нового ученика: '))

# for i in range(len(list)):
#     if height > list[i]:
#         print(f'Позиция нового ученика в шеренге: {i+1}')
#         break


# from random import randint

# lst_stud = [randint(150, 250) for _ in range(10)]

# lst_stud.sort()
# lst_stud = lst_stud[::-1]
# # [start:stop:step] срезы

# new_stud = int(input('Введите рост нового студента: '))

# print(lst_stud, new_stud, sep='\n')

# for i in range(len(lst_stud)):
#     if new_stud > lst_stud[i]:
#         lst_stud.insert(i, new_stud)
#         break

# print(lst_stud)


# size = int(input('Введите рост нового человека: '))
# list = [160, 165, 170, 180, 190, 200]

# for i in range(len(list)):
#     if list[i] > size:
#         list.insert(i, size)
#         break
# print(list)
