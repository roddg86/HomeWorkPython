from controller import parseable_data, calculate
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, MessageHandler, ConversationHandler
from log import get_id_user, get_input_data, get_result, save_log

TOKEN = '5810478638:AAEYs2s-RPj-4sAyBJT5aVDKObReZulM5mU'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)

""" мозг бота """
dispatcher = updater.dispatcher

start_calc = 0


def start(update, context):
    """ Начало работы с калькулятором. Получение id пользователя """
    context.bot.send_message(update.effective_chat.id,
                             'Вас приветсвует калькулятор')

    get_id_user(update.effective_chat.id)
    return start_calc


def receiving_data(update, context):
    """ Логика бота """
    data = update.message.text
    get_input_data(data)
    list_data = parseable_data(data)
    result = calculate(list_data)
    get_result(result)
    save_log()
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')


def cancel(update, context):
    """ Закрытие бота """
    context.bot.send_message(update.effective_chat.id, 'Пока!')


""" обработчик команд """

start_handler = CommandHandler('start', start)
receiving_data_handler = MessageHandler(
    Filters.text & (~Filters.command), receiving_data)
mes_data_handler = CommandHandler('end', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={start_calc: [
                                       receiving_data_handler]},
                                   fallbacks=[mes_data_handler])

""" бот реагирует """

dispatcher.add_handler(conv_handler)


""" старт работы """

print('старт сервера')
updater.start_polling()
updater.idle()
