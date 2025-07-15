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

class Crud:
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()

    def create(self, table_name, name, age):
        result = self._cursor.execute(
            f'insert into {table_name}(name, age) values(?, ?)',(name,int(age))
            )
        self._connection.commit()

    def read(self, table_name):
        result = self._cursor.execute(
            f'select * from {table_name}'
        ).fetchall()

        for num, name, age in result:
            print(num, name, age)

    def update(self, table_name, id_num, name=None, age=None):
        result = self._cursor.execute(
            f'update {table_name} set name="{name}", age={age} where id={id_num}'
            )
        self._connection.commit()

    def delete(self, in_mun, table_name):
        result = self._cursor.execute(
            f'delete from {table_name} where id = {in_mun}'
        )
        self._connection.commit()

    def __del__(self):
        self._cursor.close()
        self._connection.close()


db = Crud('./database/movies.sqlite')
db.delete(24, 'users')
db.create('users', 'Иван', '87')
db.update('users', 23, 'Николай', 72)
db.read('users')