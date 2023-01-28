from student_database import set_student, set_rating


def add_student():
    """ Получение данных ученика от учителя и их передача для записи """
    metric = input(
        'Введите данные (Фамилия, Имя класс через пробел): ').split(' ')
    set_student(metric)


def put_rating():
    """ Получение данных оценки от учителя и их передача для записи """
    last_name = input('Введите фамилию ученика: ')
    lesson = input('Введите название урока ')
    rating = input('Введите оценку или оценку через пробел: ').split()
    set_rating(last_name, lesson, rating)
