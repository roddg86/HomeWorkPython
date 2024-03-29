""" Модуль логирование """

from datetime import datetime as dt


def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Lectures/lec4/join_job/log.csv', 'a') as file:
        file.write('{},temperature;{}'
                   .format(time, data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Lectures/lec4/join_job/log.csv', 'a') as file:
        file.write('{},pressure;{}'
                   .format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Lectures/lec4/join_job/log.csv', 'a') as file:
        file.write('{},wind_speed;{}'
                   .format(time, data))
