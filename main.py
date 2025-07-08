# Регулярные выражения (поиск по паттерну)
# Regular Expression - папка при написании "re"
# r-строка — raw-string (сырая строка)
import re

# pattern = r'\b\w{4}\b' # -> регулярное выражение = \b начинает с
# # w любого символа, состоит {4} из 4 символов и \b заканчивает
# test_string = 'дома было холодно'
#
# result = re.search(pattern, test_string) # ищет только первое значение <re.Match object; span=(0, 4), match='дома'>
# print(result) # -> <class 're.Match'>
# result = re.findall(pattern, test_string) # ['дома', 'было']
# print(result)

# pattern = r'\d'
# test_string = 'телефон 112'
# result = re.findall(pattern, test_string)
# print('Цифры есть') if result else print('Цифр нет')

# pattern = r'\d{3}'
# test_string = 'телефон 112'
# result = re.findall(pattern, test_string)
# print(result)

# pattern = r'начало!\Z'
# test_string = 'Главное - начало!'
# result = re.findall(pattern, test_string) # -> ['начало!']
# print(result)

# pattern ='[0-5][0-9]'  # -> ['12', '59']
# test_string = 'Время - 12:59'
# result = re.findall(pattern, test_string)
# print(result)
#
# pattern = '[а-яА-Я]' # -> ['В', 'р', 'е', 'м', 'я']
# test_string = 'Время - 12:59'
# result = re.findall(pattern, test_string)
# print(result)

# pattern = '[^емя:]' # -> ['В', 'р', ' ', '-', ' ', '1', '2', '5', '9']
# test_string = 'Время - 12:59'
# result = re.findall(pattern, test_string)
# print(result)

pattern = r'\((.+?)\)' # -> ['pattern'] -- (.+?) "." - любой символ, "+?" повторяется 1 и более раз
test_string = 'Поиск по образцу (pattern)'
result = re.findall(pattern, test_string)
print(result)

pattern = r'\((.*)\)' # -> ['pattern'] -- (.*) "." - любой символ, "*" от нуля до бесконечности
test_string = 'Поиск по образцу (pattern)'
result = re.findall(pattern, test_string)
print(result)

# pattern = 'o{2,5}' # -> ['oo', 'ooo', 'ooooo', 'ooooo', 'oo']
# test_string = 'Gogle1, Google2, Gooogle3, Goooooole6, Gooooooole7'
# result = re.findall(pattern, test_string)
# print(result)

# pattern = 'Go{2,}gle' # -> ['Google', 'Gooogle']
# test_string = 'Gogle, Google, Gooogle'
# result = re.findall(pattern, test_string)
# print(result)