from methods import add, sub, div, mult


def parseable_data(data):
    """ Получение уравнения в виде строки и преобразование в список (парсинг)
    пример: 1+(1+3-2*(2/3)) -> ['1', '+', '(', '1', '+', '3', '-', '2', '*', '(', '2', '/', '3', ')', ')'] """
    math_equation = []
    math_elem = []
    for i in data:
        if i.isdigit():
            math_elem.append(i)
        elif (not i.isdigit()) and math_elem:
            math_equation.append(int(''.join(math_elem)))
            math_equation.append(i)
            math_elem = []
        elif (not i.isdigit()) and (not math_elem):
            math_equation.append(i)
    if math_elem:
        math_equation.append(int(''.join(math_elem)))
    return math_equation


def calculate(part_list):
    """ Вычисление примера, полученного в виде списка """
    result = 0
    if len(part_list) == 1:
        return part_list[0]
    for s in part_list:
        if s == '*' or s == '/':
            # вычисление умножения
            if s == '*':
                index = part_list.index(s)
                result = mult(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + \
                    [result] + part_list[index + 2:]
            # вычисление деления
            else:
                index = part_list.index(s)
                result = div(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + \
                    [result] + part_list[index + 2:]

    for s in part_list:
        if s == '+' or s == '-':
            # вычисление сложения
            if s == '+':
                index = part_list.index(s)
                result = add(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + \
                    [result] + part_list[index + 2:]
            # вычисление вычитания
            else:
                index = part_list.index(s)
                result = sub(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + \
                    [result] + part_list[index + 2:]
    return result
