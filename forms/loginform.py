from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Логин', validators=[DataRequired('Обязательно для заполнения')])
    password = PasswordField('Пароль', validators=[DataRequired('Без пароля не пройдешь')])
    remember_me = BooleanField('Запомнить данные')
    submit = SubmitField('Войти')
