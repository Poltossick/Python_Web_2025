class Sorter:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    # def delete_word(self, word):
    #     if

    def result(self):
        return sorted(self.words, key=lambda x: len(x))


class Separator:
    def __init__(self):
        self._odd = [] # нечетные
        self._even = [] # четные

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
        self._counter +=1

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
        return f'Имя — {self._name}'

    def get_age(self):  # getter
        return f'Возраст — {self._age}'

    def person_info(self):
        print(f'Данные пользователя:\nИмя - {self._name}, возраст {self._age}')

    # __________________________________________________________________________________
    def summ(a, b):
        return a + b


def diff(a, b):
    return a - b

# print(__name__)
