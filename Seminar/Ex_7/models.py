""" Основные функции программы.
предоставляет данные и реагирует на команды контроллера, 
изменяя своё состояние. """

""" Функция добавляет пробелы в результирующую строку между действиями,
разделяет делая наш результат списком,
преобразует все числовые значения в числа. """


def get_steps_lst(in_data: str):
    res = ''

    for el in in_data:
        if el.isdigit():
            res += el
        else:
            res += f' {el} '

    res = res.split()

    for i in range(len(res)):
        if res[i].isdigit():
            res[i] = int(res[i])

    return res


""" Функция считает количество действий """


def get_steps_count(lst_in: list):
    count = 0

    for el in lst_in:
        if type(el) == str:
            count += 1

    return count


""" Функция вычисляет поданые значение из списка,  возвращает новый список """


def process_step(lst_in: list):
    lst_work = lst_in[:]  # lst_in.copy()
    if ('/' in lst_work) or ('*' in lst_work):
        for i in range(len(lst_work)):
            if lst_work[i] == '/':
                temp = lst_work[i-1]/lst_work[i+1]
                del lst_work[i - 1: i + 2]
                lst_work.insert(i - 1, temp)
                break

            elif lst_work[i] == '*':
                temp = lst_work[i - 1] * lst_work[i + 1]
                del lst_work[i - 1: i + 2]
                lst_work.insert(i - 1, temp)
                break
    else:
        for i in range(len(lst_work)):
            if lst_work[i] == '+':
                temp = lst_work[i - 1] + lst_work[i + 1]
                del lst_work[i - 1: i + 2]
                lst_work.insert(i - 1, temp)
                break

            elif lst_work[i] == '-':
                temp = lst_work[i - 1] - lst_work[i + 1]
                del lst_work[i - 1: i + 2]
                lst_work.insert(i - 1, temp)
                break

    return lst_work


if __name__ == '__main__':
    # print(process_func('1100/25-22*3/2+120*8'))
    print('')
