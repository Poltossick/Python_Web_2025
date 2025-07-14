# CSV-файлы

import csv
from os import write

data = [
    ['name', 'age', 'city'],
    ['Petr', '28', 'Moscow'],
    ['Boris', '57', 'Magadan'],
    ['Oleg', '42', 'Abakan'],
    ['Ivan', '22', 'Omsk']
]

with open('people.csv', 'r', encoding='utf-8') as f1:
    reader = csv.reader(f1, delimiter=',', quotechar='"')
    for row in reader:
        print(row)

with open('employee.csv', 'w', newline='', encoding='utf-8') as f2:
    writer = csv.writer(f2)
    writer.writerows(data)
