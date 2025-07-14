# JSON - (JavaScript Object Notation)
#  Для чтения load() - читает из файла
#  Для чтения loads() - читает строковое представление будущего объекта

import json

fruits = {
    'ананас': 300,
    'банан': 150,
    'яблоко': 120,
    'апельсин': 170,
}

with open ('fruits.json', 'wt', encoding='utf-8') as frt:
    json.dump(fruits, frt, indent=4)

# data = json.dumps(fruits, indent=4)
# print(data)
#
# char_code = 0x0441
# character = chr(char_code)
# print(character)