# from telegram import Bot
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
# from random import randint

# A = 0
# B = 1

# bot = Bot(token='5810478638:AAEYs2s-RPj-4sAyBJT5aVDKObReZulM5mU')
# updater = Updater(token='5810478638:AAEYs2s-RPj-4sAyBJT5aVDKObReZulM5mU')

# """ мозг бота """
# dispatcher = updater.dispatcher


# def start(update, context):
#     context.bot.send_message(update.effective_chat.id, "Привет \n Как дела?")
#     return A


# def howareu(update, context):
#     text = update.message.text
#     if 'хорошо' in text.lower():
#         context.bot.send_message(
#             update.effective_chat.id, "Я рад, что у вас все хорошо")
#     else:
#         context.bot.send_message(
#             update.effective_chat.id, "Не грусти, все будет отлично")
#     context.bot.send_message(update.effective_chat.id, "Какая у тебя погода?")
#     return B


# def weather(update, context):
#     text = update.message.text
#     context.bot.send_message(update.effective_chat.id,
#                              "У меня сегодня такая же погода")
#     context.bot.send_message(update.effective_chat.id,
#                              "Мне пора бежать, пока!")
#     return ConversationHandler.END


# def cancel(update, context):
#     context.bot.send_message(update.effective_chat.id,
#                              "Что то пошло не так")


# # def rand(update, context):
# #     context.bot.send_message(update.effective_chat.id, f'{randint(1,100)}')


# # def default(update, context):
# #     context.bot.send_message(update.effective_chat.id,
# #                              "Я незнаю таких команд")


# # def default_voice(update, context):
# #     context.bot.send_message(update.effective_chat.id,
# #                              "Я не умею разговаривать")


# # def privet(update, context):
# #     text = update.message.text
# #     if 'прив' in text.lower():
# #         context.bot.send_message(update.effective_chat.id,
# #                                  "И тебе привет мой дорогой друг")
# #     else:
# #         context.bot.send_message(update.effective_chat.id,
# #                                  "Я тебя не понимаю")


# """ обработчик команд """

# start_handler = CommandHandler('start', start)
# howareu_handler = MessageHandler(Filters.text, howareu)
# weather_handler = MessageHandler(Filters.text, weather)
# cancel_handler = CommandHandler("cancel", cancel)
# # random_handler = CommandHandler('random', rand)
# # default_handler = MessageHandler(Filters.command, default)
# # default_voice_handler = MessageHandler(Filters.voice, default_voice)
# # privet_handler = MessageHandler(Filters.text, privet)
# conv_handler = ConversationHandler(entry_points=[start_handler],
#                                    states={A: [howareu_handler],
#                                            B: [weather_handler]},
#                                    fallbacks=[cancel_handler])

# """ бот реагирует """

# # dispatcher.add_handler(start_handler)
# # dispatcher.add_handler(random_handler)
# # dispatcher.add_handler(default_handler)
# # dispatcher.add_handler(default_voice_handler)
# # dispatcher.add_handler(privet_handler)
# dispatcher.add_handler(conv_handler)

# """ старт работы """

# print('старт сервера')
# updater.start_polling()
# updater.idle()
