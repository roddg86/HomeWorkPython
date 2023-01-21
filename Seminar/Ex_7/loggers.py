""" Модуль логирования """

from datetime import datetime

""" Функция логирования, записывает текущее время и дату, 
дальше открыват файл по пути,  """


def logger(data,  file_path='log.csv', func_name=None):
    time = datetime.now()
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'{time};{func_name};{data}\n')
