from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5810478638:AAEYs2s-RPj-4sAyBJT5aVDKObReZulM5mU')
updater = Updater(token='5810478638:AAEYs2s-RPj-4sAyBJT5aVDKObReZulM5mU')

""" мозг бота """
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Привет!\nНапиши мне что-нибудь, а я удалю все слова, содержащие "абв"\n')


def edit_msg(update, context):
    text = update.message.text
    text = ''.join(
        [(' '.join(list(filter(lambda x: 'абв' not in x.lower(), text.split()))))])
    context.bot.send_message(update.effective_chat.id, text)


""" обработчик команд """

start_handler = CommandHandler('start', start)
edit_msg_handler = MessageHandler(Filters.text, edit_msg)

""" бот реагирует """

dispatcher.add_handler(start_handler)
dispatcher.add_handler(edit_msg_handler)


""" старт работы """

print('старт сервера')
updater.start_polling()
updater.idle()
