# Базы данных (чтение)
"""
1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работаем в БД (запросы, ответы)
5. Отключаемся от БД
"""
import sqlite3

connection = sqlite3.connect('./database/movies.sqlite')
cursor = connection.cursor()
result = cursor.execute(
    """
    select title, year
    from films
    where genre = (
    select id from genres
    where title = 'ужасы')
    and duration between 45 and 90
    and title like 'С_к%'
    order by duration
    """
)
array = result.fetchall()

for title, year in array:
    print(title, year)
