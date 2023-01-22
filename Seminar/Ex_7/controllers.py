""" Контроллер интерпретирует действия пользователя, оповещая модель о необходимости изменений """

from models import get_steps_lst, get_steps_count, process_step
from views import step_view, process_view
from loggers import logger

""" Функция обработки всех данных и вывода их на экран """


def process_func(values: str):
    lst_steps = get_steps_lst(values)
    logger(lst_steps, func_name='get_steps_lst')

    count_steps = get_steps_count(lst_steps)
    logger(count_steps, func_name='get_steps_count')
    res_lst = lst_steps[:]

    for _ in range(count_steps):
        res_lst = process_step(res_lst)
        step_view(values, res_lst)
        logger(res_lst, file_path='Seminar/EX_7/steps.csv', func_name='process_step')

    process_view(values, res_lst[0])
    logger(res_lst[0], func_name='process_func')
    return res_lst[0]
