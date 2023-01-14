# def f(x):
#     return x**2


# g = f

# print(type(f))
# print(type(g))

# print(f(2))
# print(g(2))


def calc1(x):
    return x+10


print(calc1(10))


def calc2(x):
    return x*10


print(calc2(10))


def math(op, x):
    print(op(x))


math(calc2, 10)
math(calc1, 10)


def mylt(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)


""" Лямбда """

# сумма
# def sum(x, y):
#     return x+y

# Лямбда (та же функция сумма только через лямбда)
# sum = lambda x, y: x+y


# пробрасываем лямбду
calc(lambda x, y: x+y, 4, 9)


""" List comrehension
Создание списков, упрощенное
 """
# list[]

# for i in range(1, 101):
#     if (i % 2 == 0):
#         list.append

# print(list)


def f(x):
    return x**3


# list = [(i, f(i)) for i in range(1, 21) if (i % 2 == 0)]
print(list)


""" lamda и list comrehensions для упрощения """


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x**2), res)

print(res)

""" функция map """

li = [x for x in range(1, 20)]
li = list(map(lambda x: x+10, li))

print(li)

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = list(map(int, str_nums))
print(int_nums)

# data = list(map(int, input().split()))
# print(data)

""" функция filter """

data = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data))
print(res)

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))

print(res)

""" функция zip """

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)

""" функция enumerate """

data = list(enumerate(users))
print(data)
