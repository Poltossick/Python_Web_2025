# Введение во Flask
import os.path
from openpyxl.styles.builtins import title
from forms.loginform import LoginForm
from flask import Flask, url_for, request, render_template
from werkzeug.utils import secure_filename
from data import db_session
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSION = ['txt', 'pdf', 'jpg', 'png', 'csv', 'xlsx']


def allowed_file(filename):
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION)


@app.route('/index')
@app.route('/')
def index():
    params = {}
    params['user'] = 'аноним'
    params['title'] = 'приветствие'
    params['weather'] = 'сегодня жара'
    return render_template('index.html', **params)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return index()
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/numbers/<int:number>')
def odd_even(number):
    return render_template('numbers.html',
                           title='Чет-нечет', number=number)


@app.route('/deals')
def deals():
    deal = ['Помыть посуду', 'Выгулять собаку',
            'Снять показания счетчика', 'Оплатить коммуналку']
    return render_template('printlist.html',
                           deals=deal)


@app.route('/queue')
def queue():
    return render_template('vars.html',
                           title='Электронная очередь')


# @app.route('/countdown')
# def countdown():
#     lst = [str(x) for x in reversed(range(10))]
#     lst.append('Полетели')
#     return '<br>'.join(lst)
#
#
# @app.route('/image')
# def show_image():
#     return f'<img src="{url_for('static', filename='img/python.jpg')}">'
#
#
# @app.route('/sample-page')
# def sample_page():
#     return f"""<!doctype html>
#             <html lang="ru">
#             <head>
#                 <meta charset="UTF-8">
#                 <meta name="viewport"
#                       content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
#                 <meta http-equiv="X-UA-Compatible" content="ie=edge">
#                 <title>Картинка Том и Джерри</title>
#             </head>
#             <body>
#              <img src="{url_for('static', filename='img/python.jpg')}" alt="Python">
#             </body>
#             </html>
#     """
#
#
# @app.route('/sample-page2')
# def sample_page2():
#     with open('temp.html', 'r', encoding='utf-8') as html:
#         return html.read()
#
# """
# x = 5 #  так делать нельзя
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)
# """
#
# """
# <string> - по умолчанию строка
# <int:number> - целое число
# <float:number> - десятичное число
# <path:p> - может содержать слэши для указания пути
# <uuid:id> - строка-идентификатор (16-байт в HEX-формате)
# """
#
#
# @app.route('/greeting/<user>/<int:id_num>')
# def greeting(user, id_num):
#     return f'Добро пожаловать, {user} с id={id_num}'
#
# import sqlite3
#
# @app.route('/get-users/<int:id_num>')
# def get_users(id_num):
#     connection = sqlite3.connect('./static/database/movies.sqlite')
#     cursor = connection.cursor()
#     query = cursor.execute(
#         f"""
#         select name, city from users
#         where trip_id = {id_num}
#         """
#     )
#     array = query.fetchall()
#     name, city = array[len(array)-1]
#     cursor.close()
#     connection.close()
#     return f'{name}, {city}'

# @app.route('/get-users2/<city>')
# def get_users2(city):
#     connection = sqlite3.connect('./static/database/movies.sqlite')
#     cursor = connection.cursor()
#     query = cursor.execute(
#         """
#         select name, city from users
#         where city = ?
#         """,(str(city),)
#     ).fetchall()
#     for k, v in enumerate(query):
#         return f'{k}, {v}'
#     cursor.close()
#     connection.close()

# @app.route('/form-test', methods=['POST', 'GET'])
# def form_test():
#     if request.method == 'GET':
#         with open('form.html', 'r', encoding='utf-8') as html:
#             return html.read()
#     elif request.method == 'POST':
#         print(request.form['gender'])
#         print(request.form['email'])
#         return 'Форма успешно отправлена'

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'GET':
        with open('old/upload.html', 'r', encoding='utf-8') as html:
            return html.read()
    elif request.method == 'POST':
        if 'file' not in request.files:
            return 'Файл не был выбран'

        file = request.files['file']

        if file.filename == '':
            return 'Файл не был выбран'

        if file and allowed_file(file.filename):
            new_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_name))
            return f'Файл {new_name} загружен успешно'
    return 'Ошибка загрузки'


if __name__ == '__main__':
    db_session.global_init('database/news.sqlite')
    app.run(host='localhost', port=5000, debug=True)
