# Области видимости

# Shadows name 'square' from outer scope - локальная переменная перекрывает глобальную,
# так как имеет больший авторитет внутри функции
PI = 3.14
words = ['check']
square = 'Дворцовая площадь'

def square_area(lenght, width):
    square = lenght * width  # нужно переименовать "square" into "area"
    print(f'Площадь площади "{square}" = {square}')  # Площадь площади "76800" = 76800


def circle_lenght(radius):
    perimetr = 2 * PI * radius
    print(f'Длина окружности с радиусом {radius} = {perimetr:.2f}')


def print_array(array: list) -> None:
    for item in array:
        print(item)


def print_array_2(array: list) -> None:
    """
    Использование внешней глобальной переменной в функции
    :param array: массив
    :return: значение из массива глобальной переменной
    """
    for item in words:
        print(item)


def greet(name):
    print('Hi,', name)
    name = 'friend'
    print('Hello,', name)


def main():
    """
    константы -> функции -> def main(): переменные, вызов функций
    :return: возвращает все вызовы
    """
    text = ['test'] # псевдо-глобальное
    square_area(320, 240)
    circle_lenght(5)
    print_array(text)
    print_array_2(words)
    print_array_2(['a', 'b', 'c'])
    greet('Petr')  # вывод Hi, Petr // Hello, friend - так как переназначили name


main()
print('Давай встретимся, где ', square)
print('Ну что встречаемся, где ', square)