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





