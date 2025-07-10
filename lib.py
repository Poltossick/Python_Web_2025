

class SquareFunction:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __call__(self, x):
        return self._a * x ** 2 + self._b * x + self._c

class MyTime:
    def __init__(self, minutes, seconds):
        if 0 <=  minutes < 60:
            self._minutes = minutes
        if 0 <=  seconds < 60:
            self._seconds = seconds

    def __str__(self):
        return f'<Time: {self._minutes}:{self._seconds}>'

    def __add__(self, other):
        # if self._seconds + other._seconds >= 60:
        #     return f'{self._minutes + other._minutes + 1} мин., {self._seconds + other._seconds - 60} сек.'
        # else:
        #     return f'{self._minutes + other._minutes} мин., {self._seconds + other._seconds} сек.'
        m = self._minutes + other._minutes
        s = self._seconds + other._seconds
        m += s // 60
        s = s % 60
        m = m % 60
        # return f'{m} мин., {s} сек.'
        return f'{m:02}:{s:02}'

from math import hypot

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self): # -> переопределение метода, для простой строки
        return f'<Point: ({self.x}, {self.y})>'

    def __repr__(self): # -> предоставление метода для читабельности, для списка объектов
        return f'<Point: ({self.x}, {self.y})>'

    def __sub__(self, other):
        return Point(abs(self.x - other.x), abs(self.y - other.y))

    def __add__(self, other):
        return hypot(self.x - other.x, self.y - other.y)




class Stat:
    def __init__(self, vals):
        self._values = vals[:]  # получаем копию

    def is_int(self):
        return all(isinstance(item, int) for item in self._values)

    def get_min(self):
        if self.is_int():
            return min(self._values)
        return None

    def get_max(self):
        if self.is_int():
            return max(self._values)
        return None

    def get_average(self):
        if self.is_int():
            return sum(self._values) / len(self._values)
        return None



class Selector:
    def __init__(self, vals):
        self._values = vals[:]  # получаем копию

    def get_odd(self):
        return [item for item in self._values if item % 2]

    def get_even(self):
        return [item for item in self._values if item % 2 == 0]


class Student:
    def __init__(self, name='N/A', university='N/A'):
        self._name = name
        self._university = university

    def get_university(self):
        return self._university

    def get_name(self):
        return self._name


class Employee:
    def __init__(self, name='N/A', company='N/A'):
        self._name = name
        self._company = company

    def get_company(self):
        return self._company

    def get_name(self):
        return self._name


from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def perimetr(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimetr(self):
        return (self.height + self.width) * 2

    def area(self):
        return self.height * self.width


class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_left(self, weight: int):  # в граммах
        if weight <= 0:
            print('Вес монетки не может быть меньше нуля или ноль')
        else:
            self.left += weight

    def add_right(self, weight: int):  # в граммах
        if weight <= 0:
            print('Вес монетки не может быть меньше нуля или ноль')
        else:
            self.right += weight

    def result(self) -> str:
        if self.right < self.left:
            return 'Левая монетка перевесила'
        elif self.right > self.left:
            return 'Правая монетка перевесила'
        elif self.right == self.left:
            return 'Вес монеток одинаков'


class Sorter:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def result(self):
        return sorted(self.words, key=lambda x: len(x))


class Separator:
    def __init__(self):
        self._odd = []  # нечетные
        self._even = []  # четные

    def add_num(self, num):
        if num % 2:
            # self._odd += [num]
            self._odd.append(num)
        else:
            # self._even+= [num]
            self._even.append(num)

    def get_odd(self):
        return self._odd

    def get_even(self):
        return self._even


class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def click_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0


class Car:
    count = 0

    def __init__(self, brand='N/A', model='N/A', color='N/A'):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_on = False
        Car.count += 1

    def start_engine(self):
        self.engine_on = True  # пока не сработает

    def set_brand(self, new_brand):  # setter
        if new_brand:
            self.brand = new_brand

    def set_model(self, new_model):  # setter
        if new_model:
            self.model = new_model

    def set_color(self, new_color):  # setter
        if new_color:
            self.color = new_color

    def get_brand(self):  # getter
        return f'Бренд авто — {self.brand}'

    def get_model(self):  # getter
        return f'Модель авто — {self.model}'

    def get_color(self):  # getter
        return f'Цвет авто — {self.color}'

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand} {self.model}')
        else:
            print('Заведите автомобиль')

    @staticmethod
    def get_count():
        return Car.count


# __________________________________________________________________________________
class Person:
    def __init__(self, name='N/A', age='N/A'):
        self._name = name
        self._age = age

    def set_name(self, new_name):  # setter
        if new_name:
            self._name = new_name

    def set_age(self, new_age):  # setter
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print('Некорректный возраст — ', new_age)

    def get_name(self):  # getter
        return self._name

    def get_age(self):  # getter
        return self._age

    def person_info(self):
        print(f'Data\nName - {self._name}, age {self._age}')

    # __________________________________________________________________________________
    def summ(a, b):
        return a + b


def diff(a, b):
    return a - b

# print(__name__)
