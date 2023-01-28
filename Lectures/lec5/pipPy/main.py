""" pythom телеграм бот """

from bot_commands import *

app = ApplicationBuilder().token(
    "5810478638:AAEYs2s-RPj-4sAyBJT5aVDKObReZulM5mU").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print('server start')
app.run_polling()

""" Графики """

# import matplotlib.pyplot as plt
# import numpy as np

# list = [1, 2, 3, 2, 7]
# plt.plot(list)

# plt.show()


""" Смайлики в консоли """

# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))

""" Прогресс бар с имитацией загрузки """

# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()

""" Проверка числа на четность """

# from isOdd import isOdd

# print(isOdd(0))
# print(isOdd(4))
