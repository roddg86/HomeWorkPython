""" 1) Создайте программу для игры с конфетами человек против бота.
Условие задачи: На столе лежит 120 конфет. Играют два игрока делая ход друг после друга.
Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
Победитель - тот, кто оставил на столе 0 конфет.

120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр) """

""" Вариант человек - человек """

# """ Ход первого игрока выбирается рандомно """
# """ Глобальные переменные """
# from random import randint as ri
# total_sweet = 120  # Общее количество конфет
# take_sweet = 0  # Сколько конфет будет брать игрок или бот
# player_sweet = 0  # Общее количество конфет у игрока
# bot_sweet = 0  # Общее количество конфет у бота

# """ Функция определяет правила и запускает игру"""


# def start_game():
#     print("На столе лежит 120 конфет. \n"
#           "Играют два игрока делая ход друг после друга. \n"
#           "Первый ход делает человек. \n"
#           "За один ход можно забрать не более чем 28 конфет. \n"
#           "Победитель - тот, кто оставил на столе 0 конфет. ")
#     who_is_first()


# """ Функция определяет кто будет первым ходить в игре """


# def who_is_first():
#     random_number = ri(1, 2)
#     if random_number == 1:
#         player_turn1()
#     else:
#         player_turn2()


# """ Ход игрока 1 """


# def player_turn1():
#     global total_sweet
#     global take_sweet
#     global player_sweet
#     print(f"Первый игрок Ваш ход, сейчас на столе {total_sweet} конфет")
#     take_sweet = int(input("Сколько конфет вы хотите взять?: "))
#     while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
#         take_sweet = int(
#             input("Вы берете слишком много конфет! Попробуйте снова: "))
#     total_sweet -= take_sweet
#     player_sweet += take_sweet
#     if total_sweet > 0:
#         player_turn2()
#     else:
#         print("Вы победили! Игрок 1")


# """ Ход игрока 2 """


# def player_turn2():
#     global total_sweet
#     global take_sweet
#     global player_sweet
#     print(f"Второй игрок Ваш ход, сейчас на столе {total_sweet} конфет")
#     take_sweet = int(input("Сколько конфет вы хотите взять?: "))
#     while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
#         take_sweet = int(
#             input("Вы берете слишком много конфет! Попробуйте снова: "))
#     total_sweet -= take_sweet
#     player_sweet += take_sweet
#     if total_sweet > 0:
#         player_turn1()
#     else:
#         print("Вы победили! Игрок 2")


# start_game()

""" Вариант человек - компьютер """

# """ Ход первого игрока выбирается рандомно """
# """ Глобальные переменные """
# from random import randint as ri
# total_sweet = 120  # Общее количество конфет
# take_sweet = 0  # Сколько конфет будет брать игрок или бот
# player_sweet = 0  # Общее количество конфет у игрока
# bot_sweet = 0  # Общее количество конфет у бота

# """ Функция определяет правила """


# def start_game():
#     print("На столе лежит 120 конфет. \n"
#           "Играют два игрока делая ход друг после друга. \n"
#           "Первый ход делает человек. \n"
#           "За один ход можно забрать не более чем 28 конфет. \n"
#           "Победитель - тот, кто оставил на столе 0 конфет. ")
#     who_is_first()


# """ Функция определяет кто будет первым ходить в игре """


# def who_is_first():
#     random_number = ri(1, 2)
#     if random_number == 1:
#         player_turn()
#     else:
#         bot_turn()


# """ Ход игрока """


# def player_turn():
#     global total_sweet
#     global take_sweet
#     global player_sweet
#     print(f"Ваш ход, сейчас на столе {total_sweet} конфет")
#     take_sweet = int(input("Сколько конфет вы хотите взять?: "))
#     while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
#         take_sweet = int(
#             input("Вы берете слишком много конфет! Попробуйте снова: "))
#     total_sweet -= take_sweet
#     player_sweet += take_sweet
#     if total_sweet > 0:
#         bot_turn()
#     else:
#         print("Вы победили!")


# """ Ход компьютера """


# def bot_turn():
#     global total_sweet
#     global take_sweet
#     global bot_sweet
#     take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1, 28) # интеллект бота
#     total_sweet -= take_sweet
#     bot_sweet += take_sweet
#     print(
#         f"Бот взял {take_sweet} конфет! На столе осталось {total_sweet} конфет")
#     if total_sweet > 0:
#         player_turn()
#     else:
#         print("Бот победил! Восстание машин")


# start_game()

""" 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

1 | 2 | X
4 | X | O
X | 8 | O """

# """ Инициализация карты """
# maps = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 9]

# """ Инициализация победных линий """
# victories = [[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [0, 3, 6],
#              [1, 4, 7],
#              [2, 5, 8],
#              [0, 4, 8],
#              [2, 4, 6]]

# """ Вывод карты на экран """


# def print_maps():
#     print(maps[0], end=" ")
#     print(maps[1], end=" ")
#     print(maps[2])

#     print(maps[3], end=" ")
#     print(maps[4], end=" ")
#     print(maps[5])

#     print(maps[6], end=" ")
#     print(maps[7], end=" ")
#     print(maps[8])

# """ Сделать ход в ячейку """


# def step_maps(step, symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol

# """ Получить текущий результат игры """


# def get_result():
#     win = ""

#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"

#     return win


# """ Основная программа """
# game_over = False
# player1 = True

# while game_over == False:

#     # 1. Показываем карту
#     print_maps()

#     # 2. Спросим у играющего куда делать ход
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Человек 2, ваш ход: "))

#     step_maps(step, symbol)  # делаем ход в указанную ячейку
#     win = get_result()  # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False

#     player1 = not (player1)

# # Игра окончена. Покажем карту. Объявим победителя.
# print_maps()
# print("Победил", win)

""" 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные данные хранятся в отдельных текстовых файлах.
stroka = "aaabbbbccbbb"
....
stroka = "3a4b2c3b"

Вывод: stroka = "aaabbbbccbbb" """


# """ Функция считывает данные из поданного файла """


# def read_from_file(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         return file.read()

# """ Функция записывает данные в файл, на вход подается имя файла и данные """


# def write_to_file(filename, data):
#     with open(filename, 'w', encoding='utf-8') as file:
#         return file.write(data)

# """ Функция сжатия данных, запаковка """


# def compression(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# """ Функция распаковки данных, декодирование """


# def decompression(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# print("==========СЖАТИЕ ТЕКСТА===========")
# text_to_compressed = read_from_file("text_to_compress.txt")
# print(text_to_compressed)
# compressed_text = compression(text_to_compressed)
# print(f"{compressed_text}\n")
# write_to_file("compressed_text.txt", compressed_text)

# print("==========РАСПАКОВКА ТЕКСТА===========")
# compressed_text = read_from_file("compressed_text.txt")
# print(compressed_text)
# decompressed_text = decompression(compressed_text)
# print(decompressed_text)
# write_to_file("text_to_compress.txt", decompressed_text)
