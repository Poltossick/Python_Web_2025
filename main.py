name = 'Петр'
email = 'petr@r.ru'
age = 2025-1954
weight = 75.19

# placeholder (способ держателя места)
# $s - string (строка)
# %d - digit (целое число)
# %f - float (дробь)
print('Имя: %s, Почта: %s, Возраст: %d' %(name, email, age))

# способ метод - формат
print('Имя: {}, Почта: {}, Возраст: {}' .format(name, email, age))

# способ F строка
print(f'Имя: {name}, Почта: {email}, Возраст: {age}, Вес: {weight:.1f}')
