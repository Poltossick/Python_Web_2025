# Множественный возврат - возврат нескольких значений из функции
def coordinates():
    return 5.4, 3.2, 5.6, 7.3, 6.9
print(coordinates()) # возвращает картеж tuple (5.4, 3.2, 5.6, 7.3, 6.9)
print(list(coordinates()))

x, y, *rest = coordinates()
print(f'x = {x}, y = {y}, rest = {rest}') # распаковка x = 5.4, y = 3.2, rest = [5.6, 7.3, 6.9]

x, *rest, y  = coordinates()
print(f'x = {x}, rest = {rest}, y = {y}') # распаковка x = 5.4, rest = [3.2, 5.6, 7.3], y = 6.9

*rest, y = coordinates()
print(f'rest = {rest}, y = {y}') # распаковка rest = [5.4, 3.2, 5.6, 7.3], y = 6.9

*names, surname = 'Остап Сулейман Бендер'.split()
print(names, '-', surname) # ['Остап', 'Сулейман'] - Бендер
