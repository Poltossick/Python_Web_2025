class Animal:
    def make_sound(self):
        pass

    def get_name(self):
        return 'Животное'


class Dog(Animal):
    def get_name(self):
        return 'Собака'

    def make_sound(self):
        return 'Гав-гав'

    def info(self):
        print(f'Класс: {self.__class__.__name__}')


class Cat(Animal):
    def get_name(self):
        return 'Кот'

    def make_sound(self):
        return 'Мяу-мяу'

    def info(self):
        print(f'Класс: {self.__class__.__name__}')


class Horse(Animal):
    def get_name(self):
        return 'Конь'

    def make_sound(self):
        return 'И-го-го'

    def info(self):
        print(f'Класс: {self.__class__.__name__}')


class Zoo(Dog, Cat, Horse):
    def zoo_animals(self):
        print(f'Класс животного в зоопарке: '
              f'{[base.__name__ for base in self.__class__.__bases__]}')

    def make_all_sounds(self):
        sounds = []
        for base in self.__class__.__bases__:
            if hasattr(base, 'make_sound'): # hasattr - проверяет, существует атрибут
                # или метод у объекта.
                sounds.append(base.make_sound(self))
        return f'Звуки животных: {', '.join(sounds)}'

    def all_animals(self):
        return (f'В зоопарке есть: '
                f'{', '.join([base.get_name(self)
                for base in self.__class__.__bases__ 
                if hasattr(base, 'get_name')])}')




class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_left(self, weight: int) -> int:  # в граммах
        self.left += weight

    def add_right(self, weight: int) -> int:  # в граммах
        self.right += weight

    def result(self) -> str:
        if self.right < self.left:
            return 'Левая монетка перевесила'
        elif self.right > self.left:
            return 'Правая монетка перевесила'
        else:
            return 'Вес монеток одинаков'
