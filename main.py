# Базы данных (чтение)
"""
1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работаем в БД (запросы, ответы)
5. Отключаемся от БД
"""
import sqlite3
import csv

connection = sqlite3.connect('./database/movies.sqlite')
cursor = connection.cursor()
with open ('people.csv', 'rt', encoding='utf-8') as f1:
    reader = csv.reader(f1, delimiter=',')
    next(reader)
    for name, age in reader:
        cursor.execute(
            """
            insert into
            users(name, age)
            values(?, ?)
            """,(name, int(age))
        )



connection.commit()
connection.close()
