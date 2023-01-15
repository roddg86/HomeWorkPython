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


""" 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные данные хранятся в отдельных текстовых файлах.
stroka = "aaabbbbccbbb"
....
stroka = "3a4b2c3b"

Вывод: stroka = "aaabbbbccbbb" """
