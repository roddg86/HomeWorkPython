print('hello world')

# типы данных и переменная
# int, float, boolean, str, list, None

value = None
print(type(value))

a = 123
b = 1.23
print(type(a))
print(type(b))

value = 12334
print(type(value))

s = "hello 'world' S"
print(s)

s2 = 'hello \'world S'
print(s2)

# способы вывода
print(a, '-', b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
# интерполяция
print(f'{a} - {b} - {s}')


# логические переменные
f = True
print(f)

# массив
list = []
list2 = ['1', '2', '3', 'hello']
print(list)
print(list2)

# считывание данных от пользователя

#print('Введите а')
#a = int(input())
#print('Введите b')
#b = int(input())
print(a, b)
print(a, ' + ', b, ' = ', a + b)

# арифметические операции
# +, -, *, /, %, //, **
# **, *, /, //, %, +, -
# (), Сокращенные операции

# a = +123
#b = -321
a = 1.312312
b = 3
c = round(a * b, 3)
print(c)

# логические операции
# >, >=, <, <=, ==, !=
# not, and, or -не путать с &, |, ^
# is, is not, in, not in

a = 1 > 4
b = 1 < 3 < 5 < 10
print(a)
print(b)

func = 1
T = 4
x = 123
print(func < T > (x))

f = 1 > 2 or 4 < 6
print(f)

f = [1, 2, 3, 4]
print(f)
print(not 2 in f)
is_odd = not f[0] % 2
print(is_odd)

# Управляющие конструкции
# if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введте имя: ')
if username == 'Маша':
    print('Ураб это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)


# Управляющие конструкции
# while

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(original)
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)


# Управляющие конструкции
# for

list = [1, 2, 3, 4, 5]
for i in list:
    print(i**2)

#r = range(10)
for i in range(10):
    print(i)

# Строки
text = 'сьещь ещё этих мягких французских булок'
print(len(text))
print('ещё' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('еще', 'ЕЩЁ'))

for c in text:
    print(c)

# срезы
text = 'съешь ещё этих мягких французских булок'
print(text[0])  # c
print(text[1])  # ъ
print(text[len(text)-1])  # к
print(text[-5])  # б
print(text[:])  # print(text)
print(text[:2])  # съ
print(text[len(text)-2:])  # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл

text = text[2:9] + text[-5] + text[:2]  # ...

# списки
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
ran = range(1, 6)
print(type(ran))
#numbers = list(ran)
print(type(numbers))
print(numbers)

#numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers)  # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
print(i)  # [20, 4, 6, 8, 10]
print(numbers)  # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)  # red green blue
for e in colors:
    print(e*2)  # redred greengreen blueblue
colors.append('gray')  # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # True
colors.remove('red')  # del colors[0] # удалить элемент

# Функции


def function_name(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(function_name(arg))
print(type(function_name(arg)))
