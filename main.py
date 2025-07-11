# Периодические задачи

import schedule
import datetime

i = 1

def job():
    global i
    print(f'Скрипт запустился {i} - раз')
    i += 1
    t = datetime.datetime.now()
    print(f'Время: {t.strftime('%H:%M:%S')}')


schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
