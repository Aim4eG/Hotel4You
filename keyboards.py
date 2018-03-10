from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

REMOVE_KB = ReplyKeyboardRemove()

START_KB = ReplyKeyboardMarkup([[KeyboardButton('/start')]], resize_keyboard=True)

YES_NO_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='type_of_hotel'),
                                  InlineKeyboardButton('Нет', callback_data='back_to_main')]
                                 ])

TYPE_HOTEL_KB = InlineKeyboardMarkup([
                                    [InlineKeyboardButton('Отели, минигостиницы, ботели', callback_data='th1')],
                                    [InlineKeyboardButton('Гостевые дома, апартаменты, лоджи', callback_data='th2')],
                                    [InlineKeyboardButton('Хостелы', callback_data='th3'),
                                     InlineKeyboardButton('Не важно', callback_data='th0')],
                                    [InlineKeyboardButton('Назад', callback_data='back_to_main')]
                                    ])


QUALITY_HOTEL_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Достаточно хорошо: 6+', callback_data='qh60'),
                                          InlineKeyboardButton('Хорошо: 7+', callback_data='qh70')],
                                         [InlineKeyboardButton('Очень хорошо: 8+', callback_data='qh80'),
                                          InlineKeyboardButton('Превосходно: 9+', callback_data='qh90')],
                                         [InlineKeyboardButton('Не важно', callback_data='qh0')],
                                         [InlineKeyboardButton('Назад', callback_data='type_of_hotel')]
                                         ])

NUM_STARS_KB = InlineKeyboardMarkup([[InlineKeyboardButton('1 звезда', callback_data='ns1'),
                                      InlineKeyboardButton('2 звезды', callback_data='ns2')],
                                     [InlineKeyboardButton('3 звезды', callback_data='ns3'),
                                      InlineKeyboardButton('4 звезды', callback_data='ns4')],
                                     [InlineKeyboardButton('5 звезд', callback_data='ns5'),
                                      InlineKeyboardButton('Не важно', callback_data='ns0')],
                                     [InlineKeyboardButton('Назад', callback_data='th0')]
                                     ])

GO_TRAVEL_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='go_travel'),
                                      InlineKeyboardButton('Нет', callback_data='back_to_main')]
                                     ])

CHILD_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='amount_children'),
                                  InlineKeyboardButton('Нет', callback_data='add_params')]
                                 ])

ADD_PARAMETERS_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Хочу', callback_data='yes_add_params'),
                                           InlineKeyboardButton('Не хочу', callback_data='go_travel_no_add_params')]
                                          ])

RECEPTION_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='yes_reception'),
                                      InlineKeyboardButton('Нет', callback_data='no_reception')]
                                     ])

BREAKFAST_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='yes_breakfast'),
                                      InlineKeyboardButton('Нет', callback_data='no_breakfast')]
                                     ])

WIFI_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='yes_wifi'),
                                 InlineKeyboardButton('Нет', callback_data='no_wifi')]
                                ])

PARKING_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='yes_parking'),
                                    InlineKeyboardButton('Нет', callback_data='no_parking')]
                                   ])

POOL_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='yes_pool'),
                                 InlineKeyboardButton('Нет', callback_data='no_pool')]
                                ])

DISABLED_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='yes_disabled'),
                                     InlineKeyboardButton('Нет', callback_data='no_disabled')]
                                    ])

PETS_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Да', callback_data='yes_pets'),
                                 InlineKeyboardButton('Нет', callback_data='no_pets')]
                                ])
