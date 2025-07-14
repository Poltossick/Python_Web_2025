# CSV-файлы

import csv

# with open('people.csv', 'r', encoding='utf-8') as f1:
#     dict_reader = csv.DictReader(f1)
#     for row in dict_reader:
#         print(f'{row['name']} is from {row['city']}')
#
# data = {
#     'name': 'Egor',
#     'age': 18,
#     'city': 'Tomsk'
# }
#
# field_names = ['name', 'age', 'city']
#
# with open('file.csv', 'w', newline='', encoding='utf-8') as f2:
#     writer = csv.DictWriter(f2, fieldnames=field_names)
#     writer.writerow(data)

# Режимы квотирования
data = ['name', 25, 'city']
with open('sample.csv', 'w', newline='', encoding='utf-8') as f3:
    writer = csv.writer(f3, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(data)