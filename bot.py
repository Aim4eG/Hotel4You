import logging

from telegram import Location
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, MessageHandler, RegexHandler

import config
import keyboards

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start_greeting(bot, update, chat_data):
    chat_data.clear()
    update.message.reply_text('Привет! Я помогу тебе быстро подобрать отличный отель с помощью сервиса booking.com.', reply_markup=keyboards.REMOVE_KB)
    update.message.reply_text('Если ты готов - просто напиши мне любое сообщение')

def start_description(bot, update, chat_data):
    bot.send_message(update.message.chat_id, text='Рад твоему сообщению!')
    bot.send_message(update.message.chat_id, text='Как я уже говорил, я использую сервис booking.com, как наиболее надежный и удобный сервис.')
    bot.send_message(update.message.chat_id, text='Все бронирования ты будешь делать на booking.com самостоятельно, а я отберу для тебя отели согласно твоим личным предпочтениям.')
    bot.send_message(update.message.chat_id, text='Если ты не останавливаешься в хостелах – ты больше не увидишь их в своем списке отелей, но, если захочешь, я буду показывать тебе только хостелы.')
    bot.send_message(update.message.chat_id, text='Я не буду просить дополнительную комиссию, все цены – согласно ценам на booking.com, обязательно проверь!')
    bot.send_message(update.message.chat_id, text='Чтобы подобрать лучшие варианты, мне нужно задать тебе несколько вопросов. Давай попробуем?)',
                     reply_markup=keyboards.YES_NO_KB)

def type_of_hotel(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Отлично! Где ты предпочитаешь останавливаться? Выбери один из возможных вариантов ниже:',
                          reply_markup=keyboards.TYPE_HOTEL_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

def quality_of_hotel(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Какой рейтинг должен быть у отеля? Выбери один из возможных вариантов ниже:',
                          reply_markup=keyboards.QUALITY_HOTEL_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

def num_stars(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='А сколько звезд? Выбери один из возможных вариантов ниже:',
                          reply_markup=keyboards.NUM_STARS_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

def save_parameters(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Отлично! Теперь я смогу подобрать для тебя хорошие варианты проживания. Поробуем?',
                          reply_markup=keyboards.GO_TRAVEL_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

def go_travel(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Отлично! Куда и когда ты собираешься в следующий раз? Напиши мне город и дату.',
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def back_to_main(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Хорошо! Обращайся в любое время!',
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
    bot.send_message(query.message.chat_id,
                     text='Нажми на кнопку снизу, как только снова захочешь начать общение с ботом',
                     reply_markup=keyboards.START_KB)


def help(bot, update):
    update.message.reply_text('Наш бот поможет найти лучшие места для отдыха!:)')
    update.message.reply_text('Наберите /start, чтобы начать')

def error(bot, update, error):
    logging.warning('Update {} caused error {}'.format(update, error))


if __name__ == '__main__':
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_greeting, pass_chat_data=True))

    dispatcher.add_handler(MessageHandler(Filters.text, start_description, pass_chat_data=True))
    dispatcher.add_handler(CallbackQueryHandler(type_of_hotel, pattern='type_of_hotel'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_main, pattern='back_to_main'))
    dispatcher.add_handler(CallbackQueryHandler(quality_of_hotel, pattern='(th1)|(th2)|(th3)|(th4)|(th5)|(th6)|(th7)|(th8)|(th9)|(th10)|(th11)|(th0)'))
    dispatcher.add_handler(CallbackQueryHandler(num_stars, pattern='(qh60)|(qh70)|(qh80)|(qh90)|(qh0)'))
    dispatcher.add_handler(CallbackQueryHandler(save_parameters, pattern='(ns1)|(ns2)|(ns3)|(ns4)|(ns5)|(ns0)'))
    dispatcher.add_handler(CallbackQueryHandler(go_travel, pattern='go_travel'))

    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()
