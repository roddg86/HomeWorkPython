""" Модуль логирования """

from datetime import datetime as dt

""" Функция логирования, записывает текущее время и дату, 
дальше открыват файл по пути,  """


def logger(file_path='HW7MVC/log.csv', func_name=None):
    time = dt.now().strftime('%d:%m:%Y-%H:%M')
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'{time};{func_name}\n')
