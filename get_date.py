import pandas
from datetime import datetime
import re

RU_MONTH_VALUES = {
    'янв': 1,
    'фев': 2,
    'март': 3,
    'апр': 4,
    'май': 5,
    'мая': 5,
    'июн': 6,
    'июл': 7,
    'авг': 8,
    'сен': 9,
    'окт': 10,
    'нояб': 11,
    'дек': 12
}


def month_to_int_value(date_str):
    for ru_month, value in RU_MONTH_VALUES.items():
        date_str = date_str.replace(ru_month, ' ' + str(value))

    return date_str + " " + str(datetime.now().year)


def day_to_int_value(date_str):
    for day, value in RU_COUNT.items():
        date_str = date_str.replace(day, str(value))

    return date_str + " "


def delete_all_signs(date_str):
    date_str = date_str.replace(".", " ")
    date_str = date_str.replace("-", " ")
    date_str = date_str.replace("/", " ")
    date_str = date_str.replace(",", " ")

    return date_str


def clear_let(date_str):
    b = "[a-яА-я]*"
    return re.sub(b, '', date_str)


def parse_date(date_str):
    try:
        date_str = day_to_int_value(date_str.lower())
        date_str = month_to_int_value(date_str.lower())
        date_str = delete_all_signs(date_str)
        date_str = clear_let(date_str)
        if len(date_str) <= 6:
            date_str += str(datetime.now().year)
        p_date = pandas.to_datetime(date_str, dayfirst=True)

        return [str(p_date.day), str(p_date.month), str(p_date.year)]

    except ValueError:
        return ['error','0', '0']





