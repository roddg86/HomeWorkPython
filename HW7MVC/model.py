import csv
from loggers import logger

""" Добавление в список """


def add_contact():
    first_name = input("Введите Фамилию ")
    name = input("Введите Имя ")
    telephone = input("Введите номер телефона ")
    description = input("Введите описание ")
    contact_data = (first_name, name, telephone, description)
    return contact_data


""" Добавить контакт в CSV"""


def add_contact_csv(abonent_first_name, abonent_name, abonent_tel, description):
    logger(func_name='Добавлен контакт')
    with open("HW7MVC/phone_book_csv", mode="a", encoding="utf-8") as data:
        file_writer = csv.writer(data, delimiter=",", lineterminator="\r")
        file_writer.writerow(
            [abonent_first_name, abonent_name, int(abonent_tel), description])
        print("_____________________  Контакт добавлен  ______________________")


""" Вывести контакт из CSV"""


def get_contact_from_cvs():
    csv_list = []
    with open("HW7MVC/phone_book_csv", encoding="utf-8") as data:
        reader_object = csv.reader(data, delimiter=',')
        for row in reader_object:
            csv_list.append(row)
            print(','.join(row))
    logger(func_name='Запрошены контакты из CSV')
    print("_____________________  Контакты отображены  ______________________")


""" Добавить контакт в TXT"""


def add_contact_txt(tuple):
    with open('HW7MVC/phone_book.txt', 'a', encoding="utf-8") as data:
        for i in tuple:
            data.write(str(i))
            data.write('\n')
            data.write('\n')
        data.write('----------------\n')


""" Показать TXT """


def get_contact_from_txt():
    with open('HW7MVC/phone_book.txt', 'r', encoding="utf-8") as data:
        for line in data:
            print(line)
    logger(func_name='Запрошены контакты из TXT')


""" Показать XML """


def get_contact_from_xml():
    with open('HW7MVC/phone_book.xml', 'r', encoding="utf-8") as data:
        for line in data:
            print(line)
    logger(func_name='Запрошены контакты из XML')


""" Удаление строки """


def delete_contact():
    print('Введите данные для удаления: ')
    del_value = input()

    with open('HW7MVC/phone_book_csv', encoding='utf-8') as data:
        lines = data.readlines()

    with open('HW7MVC/phone_book_csv', "w", encoding='utf-8') as data:
        for line in lines:
            if del_value not in line:
                data.write(line)
    print("Удален\n")

    logger(func_name='Удален контакт из CSV')


""" Проверка на число """


def input_num(text):
    while True:
        try:
            num = int(input(text))
            return num
        except:
            print("Введите число!")
