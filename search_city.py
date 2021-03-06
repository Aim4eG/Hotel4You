import xlrd
import xlwt
import urllib


def search_city(city):
    rb = xlrd.open_workbook('./cities.xlsx')
    sheet = rb.sheet_by_index(0)
    for row_num in range(sheet.nrows):
        row = sheet.row_values(row_num)
        if str(row[1]).lower() == str(city).lower():
            return row[3]
    return 'error'

def query(chat_data): #www.booking.com/searchresults.ru.html?<теги для поиска>
    if chat_data['hotel'] == '' and chat_data['quality'] == '' and chat_data['stars'] == '':
        res = 'www.booking.com/searchresults.ru.html?' + chat_data['city'] + '&aid=1433748&' + \
              chat_data['date_in'] + '&' + chat_data['date_out'] + '&no_rooms=1&group_adults=2'
        return res
    if chat_data['stars'] == '':
        res = 'www.booking.com/searchresults.ru.html?' + chat_data['city'] + '&nflt=' + chat_data['hotel'] + \
              chat_data['quality'] + '&aid=1433748&' + chat_data['date_in'] + '&' + \
              chat_data['date_out'] + '&no_rooms=1&group_adults=2'
        return res
    res = 'www.booking.com/searchresults.ru.html?' + chat_data['city'] + '&nflt=' + chat_data['hotel'] + \
          chat_data['quality'] + chat_data['stars'] + '&aid=1433748&' + chat_data['date_in'] + '&' + \
          chat_data['date_out'] + '&no_rooms=1&group_adults=2'
    return res


