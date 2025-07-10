# ООП - (polymorphism)

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


def shape_info(shape):
    if isinstance(shape, Circle):
        fig = 'круг'
    elif isinstance(shape, Square):
        fig = 'квадрат'
    elif isinstance(shape, Rectangle):
        fig = 'прямоугольник'
    print(f'Площадь фигуры "{fig}": {shape.area()}')
    print(f'Периметр фигуры "{fig}": {shape.perimetr()}')


sq = Square(10)
shape_info(sq)

cr = Circle(5)
shape_info(cr)

# shape_info(sq)

# cr = Circle(10)
# shape_info(cr)
#
# rc = Rectangle(2, 17)
# shape_info(rc)

# class Book:
#     def __init__(self, title, author):
#         self._title = title
#         self._author = author
#
#     def get_title(self):
#         return self._title
#
#     def get_author(self):
#         return self._author
#
# book = Book('Язык C++', 'Бьярн Страупструп')
#
# print(f'{book.get_title(), book.get_author()}')
