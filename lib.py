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






def summ(a, b):
    return a + b


def diff(a, b):
    return a - b

# print(__name__)
