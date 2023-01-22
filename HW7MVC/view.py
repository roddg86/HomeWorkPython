from model import input_num

""" Функция запуска программы """


def start():
    print("Выберте действие: ", end="\n")
    print("1 - Добавить контакт")
    print("2 - Вывести CSV")
    print("3 - Вывести TXT")
    print("4 - Вывести XML")
    print("5 - Удалить строку из CSV")
    print("0 - Выход")
    select = input_num("_ ")
    return select

