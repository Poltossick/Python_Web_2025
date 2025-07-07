# Documents
# Excel (openpyxl)
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Alignment

# # Создаем пустой Excel-файл
# wkbook = Workbook()
#
# worksheet = wkbook.active # открытие листа
# worksheet.title = 'Отчёт' # наименование листа
#
# wkbook.save('./documents/report.xlsx')

# # Запись данных в существующий файл
#
workbook = load_workbook('./documents/report.xlsx') # Открываем - загружаем рабочую книгу
worksheet = workbook.active # обращение к активному листу, можно обратиться по имени листа
#
# # worksheet['B1'] = 'Hello, word!'
# # worksheet.cell(row=1, column=3, value='English')
# # worksheet.title = 'NewWords' # переименовать лист
# # workbook.save('./documents/newtable.xlsx')
#
# #  Заголовки
worksheet['A1'] = 'Name'
worksheet['B1'] = 'Game'
worksheet['C1'] = 'Role'

worksheet['A1'].font = Font(bold=True, size=13)
worksheet['B1'].font = Font(bold=True, size=13)
worksheet['C1'].font = Font(bold=True, size=13)


info = [
    ['kirill', 'mobile legend', 'mid'],
    ['henry', 'dota 2', 'ADK'],
    ['rustam', 'wild rift', 'support'],
]

for row, data in enumerate(info, start=2):
    worksheet.cell(row=row, column=1, value=data[0])
    worksheet.cell(row=row, column=2, value=data[1])
    worksheet.cell(row=row, column=3, value=data[2])

workbook.save('./documents/gamers.xlsx')

# Чтение данных
# workbk = load_workbook('./documents/gamers.xlsx')
# wksheet = workbk.active
#
# rows_count = wksheet.max_row # число заполненных строк
#
# for row in wksheet.iter_rows(values_only=True):
#     name, gm, rl = row
#     print(f'Имя - {name}, Игра - {gm}, Позиция - {rl}')



