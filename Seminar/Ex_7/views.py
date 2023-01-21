""" Модуль отображения """


""" Функция отображения в консоли """


def step_view(data, step_data, delimeter='*'):
    print('\n' + (delimeter * 26))
    print(f'{data} ->> {step_data}')
    print(delimeter * 26 + '\n')


""" Функция вывода результата в консоль """


def process_view(data, result):
    print(f'{data} = {result}')
