# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)
# import math as m # -> подключение библиотеки, импортировать всю библиотеку, ДИНАМИЧЕСКИЙ
# print(dir(m)) # -> список функций для math
# from math import *  # -> подключение библиотеки, импортировать всю библиотеку, ВСЕ ВЫТЯГИВАЕМ СРАЗУ
from math import pi, cos, hypot  # -> подключение конкретных функция
from math import sin, radians  # -> подключение конкретных функция

print('Число Пи: ', pi)
print(f'Косинус 5°: ', round(cos(radians(5)), 3))
print('Синус 30°: ', round(sin(radians(30)), 2))
print('Гипотенуза: ', hypot(3, 2))
