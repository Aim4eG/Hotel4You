import xlrd
import xlwt

def search_city(city):
    rb =xlrd.open_workbook('./cities.xlsx')
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        if row[1] == city:
            return row[3]
            #print(city_id)
    return 'error'

def str_split(str):
    try:
        res = []
        str = str.replace(' ', '')
        temp = str.split(',', maxsplit=1)
        res.append(temp[0])
        res.append(temp[1].split('-', maxsplit=1)[0])
        res.append(temp[1].split('-', maxsplit=1)[1])
        return res
    except IndexError:
        return 'error'

def query(chat_data): #www.booking.com/searchresults.ru.html?<теги для поиска>
    res = 'www.booking.com/searchresults.ru.html?' + chat_data['city'] + '&' + chat_data['date1'] + \
          '&' + chat_data['date2'] + '&' + chat_data['hotel'] + '&' + chat_data['quality'] + '&' + chat_data['stars']
    return res








