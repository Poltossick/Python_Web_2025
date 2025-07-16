# Введение во Flask
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'Привет, Flask'


@app.route('/about')
def about():
    print('Вызвана функция about')
    return 'О нас'


@app.route('/countdown')
def countdown():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели')
    return '<br>'.join(lst)


@app.route('/image')
def show_image():
    return f'<img src="{url_for('static', filename='img/python.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""<!doctype html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport"
                      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Картинка Том и Джерри</title>
            </head>
            <body>
             <img src="{url_for('static', filename='img/python.jpg')}" alt="Python">
            </body>
            </html>
    """


@app.route('/sample-page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()

"""
x = 5 #  так делать нельзя
@app.route('/1') 
def show_num():
    global x
    x += 1
    return str(x)
"""

"""
<string> - по умолчанию строка
<int:number> - целое число
<float:number> - десятичное число
<path:p> - может содержать слэши для указания пути
<uuid:id> - строка-идентификатор (16-байт в HEX-формате)
"""


@app.route('/greeting/<user>/<int:id_num>')
def greeting(user, id_num):
    return f'Добро пожаловать, {user} с id={id_num}'

import sqlite3

@app.route('/get-users/<int:id_num>')
def get_users(id_num):
    connection = sqlite3.connect('./static/database/movies.sqlite')
    cursor = connection.cursor()
    query = cursor.execute(
        f"""
        select name, city from users
        where trip_id = {id_num}
        """
    )
    array = query.fetchall()
    name, city = array[len(array)-1]
    cursor.close()
    connection.close()
    return f'{name}, {city}'

@app.route('/get-users2/<city>')
def get_users2(city):
    connection = sqlite3.connect('./static/database/movies.sqlite')
    cursor = connection.cursor()
    query = cursor.execute(
        """
        select name, city from users
        where city = ?
        """,(str(city),)
    ).fetchall()
    for k, v in enumerate(query):
        return f'{k}, {v}'
    cursor.close()
    connection.close()


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
