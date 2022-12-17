""" 1) Напишите программу, которая принимает 
на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

# numberN = int(input('Введите число: '))

# factorial = 1

# for current in range(numberN):
#     current += 1
#     factorial *= current
#     print(f'{factorial}', end = ' ')


""" 2) Требуется найти наименьший натуральный 
делитель целого числа N, отличный от 1.

Пример:

Для n = 15: Ответ: 3
Для n = 35: Ответ: 5 """

# numberN = int(input("Введите целое число: "))
# denominator = 2
# while numberN % denominator: denominator += 1
# print(f"делитель числа {numberN} равен: {denominator}")

""" 3) Задайте список из (2*N+1) элементов, 
заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных ИНДЕКСАХ. 
Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

Ввод: 4
[-4, -3, -2, -1, 0, 1, 2, 3,4] """

# numberN = int(input('Введите число N: '))

# elements = []
# for i in range(2 * numberN + 1):
#     elements.append (-numberN + i)
# print (f'Список элементов от {-numberN} до {numberN}: {elements}')

# index = []
# for i in range(5):
#     index.append (int(input(f'Введите {i + 1} индекс: ')))
# print (f'Список индексов: {index}')

# product_of_elements = 1
# for i in range(len(index)):
#     specified_index = index[i]
#     product_of_elements *= elements[specified_index]
# print (f'Произведение элементов: {product_of_elements}')

""" 4)Требуется посчитать сумму чётных чисел, 
расположенных между числами 1 и N включительно. """

# numberN = int(input('Введите число: '))

# sum = 0

# for current in range(numberN):
#     current += 1
#     if current % 2 == 0:
#         sum += current
#         print(current, end=' ')

# print(f'сумма {sum}')
