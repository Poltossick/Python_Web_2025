# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)
import datetime as dtm
# print(dtm.datetime.now()) # сырое имя
# print(dtm.datetime.now().date()) # дата сегодня
# print(dtm.datetime.now().time()) # время сейчас
# print(type(dtm.datetime.now())) # класс

# strftime() - string format time

# time = dtm.datetime.now()
# ftime = time.strftime('%d/%m/%Y-%B') # -> 04/07/2025-July - день, год, месяц m - месяц числом, B - месяц словом на англ
# print(ftime)
# ftime = time.strftime('%H:%M') # -> 12:32
# print(ftime)
#
# my_time = dtm.time(15, 27, 32)
# my_day = dtm.date(2025, 12, 5).strftime('%d %B %Y')
# my_d_t = dtm.datetime.combine(dtm.date(2025, 12, 5), my_time)
# print(my_time)
# print(str(my_day))
# print(my_d_t)

date_1 = dtm.date(2025, 6, 15)
date_2 = dtm.date(2025, 7, 3)
print(date_2 - date_1)


