""" 1) Создайте программу для игры с конфетами человек против бота.
Условие задачи: На столе лежит 120 конфет. Играют два игрока делая ход друг после друга.
Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
Победитель - тот, кто оставил на столе 0 конфет.

120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр) """

# """ Вариант человек - человек """

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

# """ Вариант человек - компьютер """

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
#     # take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1, 28)  # интеллект умного бота
#     take_sweet = ri(1, 28)  # интелект простого бота
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


# board = list(range(1, 10))

# """ Вывод карты на экран """


# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print("-" * 13)


# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка уже занята!")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9.")


# """ Получить текущий результат игры """


# def check_win(board):
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
#                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False


# """ Основная программа """


# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)


# main(board)

# input("Нажмите Enter для выхода!")

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
