from pyparsing import *
from datetime import *
import pandas


def str_parse(str):
    rus_alphas = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    symbols = '/.,-'
    # alphas - встроенная библиотека латинских букв в pyparsing
    all_alphas = alphas + rus_alphas

    # Город: либо слова через пробелы, либо слова через дефис без пробела
    city_name = Word(all_alphas + ' ') ^ Word(all_alphas + '-' + all_alphas)
    # Дата: обязательно начинается с цифр! За цифрами может идти пробел + слова (16 марта)
    # или совокупность цифр с символами (17/05/2019, 17.05.2019, 17-05-2019, 17,05,2019).
    date = Word(nums + ' ' + all_alphas) ^ Word(nums + symbols)

    parser = city_name + date

    #s = ' Нижний Новгород      15/02.2018  '
    result = parser.parseString(str)

    # Удаление всех пробельных символов в начале и конце строки - функция strip()
    result[0] = result[0].strip()
    result[1] = result[1].strip()

    return result

# Выезжаем, например, сегодня, 24.02.2018
#now = datetime.now().date()
#print(now)


def night_amount(date_str, amount):
    #now = datetime.now().date()
    #count_days = timedelta(amount)
    date_in = pandas.to_datetime(date_str, dayfirst=True)
    date_out = date_in + timedelta(int(amount))
    res = []
    res.append(date_in.day)
    res.append(date_in.month)
    res.append(date_in.year)
    res.append(date_out.day)
    res.append(date_out.month)
    res.append(date_out.year)
    return res
    #print(new_date.day)

#date = night_amount(3)
#print(date)
