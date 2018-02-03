import logging

from telegram import Location
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, MessageHandler, RegexHandler

import config
import keyboards

import search_city

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start_greeting(bot, update, chat_data):
    chat_data.clear()
    update.message.reply_text('Привет! Я помогу тебе быстро подобрать отличный отель с помощью сервиса booking.com.', reply_markup=keyboards.REMOVE_KB)
    update.message.reply_text('Если ты готов - просто напиши мне любое сообщение')

    chat_data['message_type'] = 'start_description'

def text_message_handler(bot, update, chat_data):
    if chat_data['message_type'] == 'start_description':
        bot.send_message(update.message.chat_id,
                         text='Рад твоему сообщению! \n'
                              'Как я уже говорил, я использую сервис booking.com, как наиболее надежный и удобный сервис. \n'
                              'Все бронирования ты будешь делать на booking.com самостоятельно, а я отберу для тебя отели согласно твоим личным предпочтениям. \n'
                              'Если ты не останавливаешься в хостелах – ты больше не увидишь их в своем списке отелей, но, если захочешь, я буду показывать тебе только хостелы. \n'
                              'Я не буду просить дополнительную комиссию, все цены – согласно ценам на booking.com, обязательно проверь! \n'
                              'Чтобы подобрать лучшие варианты, мне нужно задать тебе несколько вопросов. Давай попробуем?)',
                         reply_markup=keyboards.YES_NO_KB)
        return

    elif chat_data['message_type'] == 'go_travel':
        bot.send_message(update.message.chat_id,
                         text='Ищем город в базе данных...')
        res = search_city.str_split(update.message.text)
        print(res)
        if res == 'error':
            bot.send_message(update.message.chat_id,
                             text='Возможно, вы ошиблись в написании запроса. Попробуйте ввести его еще раз;)')
        chat_data['city'] = search_city.search_city(res[0])
        if chat_data['city'] == 'error':
            bot.send_message(update.message.chat_id,
                             text='Город не найден. Возможно, вы ошиблись в названии. Попробуйте ввести его еще раз;)')
        else:
            chat_data['city'] = 'city=' + chat_data['city']
            bot.send_message(update.message.chat_id,
                         text=chat_data['city'])
            #ПАРСИНГ


        # Reading and using database of cities...


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

    bot.edit_message_text(text='Отлично! Теперь я смогу подобрать для тебя хорошие варианты проживания. Попробуем?',
                          reply_markup=keyboards.GO_TRAVEL_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

def go_travel(bot, update, chat_data):
    query = update.callback_query

    bot.edit_message_text(text='Отлично! Куда и когда ты собираешься в следующий раз? Напиши мне город и дату.\n'
                                'Пожалуйста, не забудь указать дату выезда:)\n'
                          'Например: Рим, 18 марта - 21 марта', # ВОТ ТУТ НАДО ОПИСАТЬ ВОЗМОЖНЫЕ ВАРИАНТЫ ВВОДА
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
    chat_data['message_type'] = 'go_travel'


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
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_error_handler(error)

    dispatcher.add_handler(MessageHandler(Filters.text, text_message_handler, pass_chat_data=True))

    dispatcher.add_handler(CallbackQueryHandler(type_of_hotel, pattern='type_of_hotel'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_main, pattern='back_to_main'))
    dispatcher.add_handler(CallbackQueryHandler(quality_of_hotel, pattern='(th1)|(th2)|(th3)|(th4)|(th5)|(th6)|(th7)|(th8)|(th9)|(th10)|(th11)|(th0)'))
    dispatcher.add_handler(CallbackQueryHandler(num_stars, pattern='(qh60)|(qh70)|(qh80)|(qh90)|(qh0)'))
    dispatcher.add_handler(CallbackQueryHandler(save_parameters, pattern='(ns1)|(ns2)|(ns3)|(ns4)|(ns5)|(ns0)'))
    dispatcher.add_handler(CallbackQueryHandler(go_travel, pattern='go_travel', pass_chat_data=True))

    updater.start_polling()
    updater.idle()
