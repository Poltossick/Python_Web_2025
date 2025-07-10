# ООП - (inheritance) наследование
from math import pi
from abc import ABC, abstractmethod

# object - класс всех классов, перво-класс

# базовый, родительский, супер-класс
class Shape(ABC):
    def info(self):
        print(f'Класс: {self.__class__.__name__}')

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimetr(self):
        return (self.height + self.width) * 2

    def area(self):
        return self.height * self.width


# производный, дочерний
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Square):
    def __init__(self, side):
        super().__init__(side)  # также можно если несколько супер-классов Square.__init__(self, side)
        self.side = side

    def area(self):
        return self.side ** 2 ** 1/3 / 4


tr = Triangle(5)
print(tr.area())
