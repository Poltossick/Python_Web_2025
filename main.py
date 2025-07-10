# ООП - (inheritance) наследование

# базовый, родительский, супер-класс
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimetr(self):
        return (self.height + self.width) * 2

    def area(self):
        return self.height * self.width


# производный, дочерний
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)



sq = Square(5)
print(sq.area())
print(sq.perimetr())