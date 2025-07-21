# Введение во Flask
import os.path
from openpyxl.styles.builtins import title
from pyexpat.errors import messages

from forms.loginform import LoginForm
from forms.news import NewsForm
from forms.user import Register
from flask import Flask, url_for, request, render_template, redirect, abort
from werkzeug.utils import secure_filename, redirect
from data import db_session
from data.users import User
from data.news import News
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

import sqlite3
from sqlite3 import Error

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'just_secret_key'
ALLOWED_EXTENSION = ['txt', 'pdf', 'jpg', 'png', 'csv', 'xlsx']


def allowed_file(filename):
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html', title='Страница не найдена')


@app.errorhandler(401)
def not_unauthorized(_):
    return redirect('/login')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', title='Ошибка авторизации',
                               message='Неверный логин или пароль')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required  # не может зайти на страницу, пока не авторизируется
def logout():
    logout_user()
    return redirect('/login')


@app.route('/personal-page')
def personal_page():
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():  # то же самое, что и request.method == 'Post'
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   message='Пароли не совпадают', form=form)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   message='Такой пользователь уже зарегистрирован', form=form)
        user = User(
            name=form.login.data,
            email=form.email.data,
            about=form.about.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html',
                           title='Регистрация', form=form)


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


@app.route('/get-user/')
@app.route('/get-user/<int:id_num>')
def get_user(id_num=None):
    try:
        # Подключение к базе данных
        con = sqlite3.connect('database/movies.sqlite')
        cur = con.cursor()

        if id_num is None:
            # Получение списка всех пользователей
            query = 'SELECT trip_id, name FROM users'
            response = cur.execute(query)
            result = response.fetchall()
            return render_template('get_user.html', users=result)

        # Получение информации о конкретном пользователе
        query = 'SELECT name, city, date_first FROM users WHERE trip_id=?'
        response = cur.execute(query, (id_num,))
        result = response.fetchone()

        if result:
            name, city, date_first = result
            return render_template('get_user.html',
                                   name=name,
                                   city=city,
                                   start=date_first)
        else:
            return "Пользователь не найден", 404

    except Error as e:
        return f"Произошла ошибка: {str(e)}", 500

    finally:
        # Гарантированное закрытие соединения
        if con:
            cur.close()
            con.close()


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


@app.route('/news')
def publicnews():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        p_news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True)).all()
    else:
        p_news = db_sess.query(News).filter(News.is_private != True).all()
    return render_template('news.html',
                           title='Новости', news=p_news)


@app.route('/newsjob', methods=['POST', 'GET'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News(title=form.title.data, content=form.content.data, is_private=form.is_private.data)
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/news')
    return render_template('/newsjob.html', title='Добавление новости', form=form)


@app.route('/newsjob/<int:id_num>', methods=['POST', 'GET'])
@login_required
def edit_news(id_num):
    form = NewsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(
            News.id == id_num, News.user == current_user
        ).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(
            News.id == id_num, News.user == current_user
        ).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/news')
        else:
            abort(404)
    return render_template('/newsjob.html', title='Редактирование новости', form=form)

@app.route('/newsdelete/<int:id_num>', methods=['POST', 'GET'])
@login_required
def delete_news(id_num):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(
        News.id == id_num, News.user == current_user
    ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/news')





if __name__ == '__main__':
    db_session.global_init('database/news.sqlite')
    app.run(host='localhost', port=5000, debug=True)
    # user = User()
    # # db_sess = db_session.create_session()
    # # user = db_sess.query(User).filter(User.id == 1).first()
    # # user.set_username('Mark')
    # # noone = db_sess.query(User).filter(User.id == 2).first()
    # # db_sess.delete(noone)
    # # db_sess.commit()
    # # print(user)
    # # user.name = 'Woman'
    # # user.about = 'WomanCat'
    # # user.email = 'woman@email.ru'
    # # db_sess = db_session.create_session()
    # # db_sess.add(user)
    # # db_sess.commit()
    # news = News()
    # db_sess = db_session.create_session()
    # users_user = db_sess.query(User).filter(User.id == 1).first()
    # # news.title = 'Погода в СПб'
    # # news.user = users_user
    # # news.content = 'Погода сегодня шикарная'
    # # users_user = db_sess.query(User).filter(User.id == 2).first()
    # for news in users_user.news:
    #     print(news)
    # # users_user.news.append(news)
    # # # db_sess.add(news)
    # # db_sess.commit()
