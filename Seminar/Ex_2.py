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
 