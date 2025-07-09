# ООП - объектно ориентированное программирование (encapsulation) - помещение объекта в капсулу
# инкапсуляция - сокрытие внутренней реализации с целью сокрытия внутренних данных

# АНАЛИЗ предыдущих вызовов
from lib import Car

car = Car('BMW', 'X5')
car.start_engine()
car.drive_to('город')

"""
УНЕСТИ В LIB.PY
class Car:
    def __init__(self, brand='N/A', model='N/A', color='N/A'):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True # пока не сработает

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand} {self.model}')
        else:
            print('Заведите автомобиль')
"""