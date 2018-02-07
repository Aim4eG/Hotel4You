import pandas
from datetime import datetime
import re

RU_MONTH_VALUES = {
    'янв': 1,
    'фев': 2,
    'март': 3,
    'апр': 4,
    'май': 5,
    'июн': 6,
    'июл': 7,
    'авг': 8,
    'сен': 9,
    'окт': 10,
    'нояб': 11,
    'дек': 12
}
Ru_Count= {
    'пер': 1,
    'вто': 2,
    'тре': 3,
    'четв': 4,
    'пято': 5,
    'шесто': 6,
    'седь': 7,
    'вось': 8,
    'девято': 9,
    'дес': 10,
    'один': 11,
    'двен': 12,
    'трина': 13,
    'четыр': 14,
    'пятнад': 15,
    'шестн': 16,
    'семн': 17,
    'восе': 18,
    'девятн': 19,
    'двад': 20,
    'двадцать пе': 21,
    'двадцать вт': 22,
    'двадцать т': 23,
    'двадцать ч': 24,
    'двадцать пя': 25,
    'двадцать ш': 26,
    'двадцать с': 27,
    'двадцать в': 28,
    'двадцать д': 29,
    'тридцато': 30,
    'тридцать': 31
}

def month_to_int_value(date_str):
    for ru_month, value in RU_MONTH_VALUES.items():
        date_str = date_str.replace(ru_month, str(value))

    return date_str + " " + str(datetime.now().year)

def day_to_int_value(date_str):
    for days, value in Ru_Count.items():
        date_str = date_str.replace(days, str(value))

    return date_str + " " #+ str(datetime.now().year)

def delete_all_signs(date_str):
    date_str = date_str.replace(".", " ")
    date_str = date_str.replace("-", " ")
    date_str = date_str.replace("/", " ")
    date_str = date_str.replace(",", " ")

    return date_str

def clear_let(date_str):
    b="[a-яА-я]*"
    return re.sub(b,'',date_str)

def parse_date(date_str):
    try:
        date_str = day_to_int_value(date_str.lower())
        date_str = month_to_int_value(date_str.lower())
        date_str = delete_all_signs(date_str)
        date_str = clear_let(date_str)
        if (len(date_str)<=6):
            date_str+=str(datetime.now().year)
        p_date = pandas.to_datetime(date_str)
        return [str(p_date.day), str(p_date.month), str(p_date.year)]
        #print(p_date)
        #print("Day = " + str(p_date.day) + " Month = " + str(p_date.month) + " Year = " + str(p_date.year))



    except ValueError:
        return ['error','0', '0']
