# JSON - (JavaScript Object Notation)
#  Для чтения load() - читает из файла
#  Для чтения loads() - читает строковое представление будущего объекта

import json

with open('dogs.json', 'r') as dog:
    data = json.load(dog)

print(data)

# print(f'Имя {data['name']}, возраст {data['age']} лет, питание {', '.join(data['meals'])}')

for i in range(len(data)):
    print(f'Питомец номер {i + 1}')
    for k, v in data[i].items():
        if type(v) == list:
            print(', '.join(v))
        else:
            print(f'{v}')


# with open('dogs.json', 'rt') as d:
#     temp = d.read()
#     data = json.loads(temp)
#     print(data)