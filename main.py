# Регулярные выражения (поиск по паттерну)
# Regular Expression - папка при написании "re"
# r-строка — raw-string (сырая строка)
import re

# pattern = r'стеклянн?ый' # вторая "н" может присутствовать, но не обязана
# test_string = 'стекляный, стеклянный, оловянный, деревянный, серебряный'
# result = re.findall(pattern, test_string)
# print(result) # -> ['стекляный', 'стеклянный']

# pattern = r'<img.*' # "жадный квантификатор" (greedy quantifier)
# test_string = 'Картинка <img src="bg.jpg"> в тексте</p>' # ['<img src="bg.jpg"> в тексте</p>']
# result = re.findall(pattern, test_string)
# print(result)
#
# pattern = r'<img.*?>' # "ленивый квантификатор" (non-greedy, lazy quantifier)
# test_string = 'Картинка <img src="bg.jpg"> в тексте</p>'  # ['<img src="bg.jpg">']
# result = re.findall(pattern, test_string)
# print(result)

# pattern = r'<img[^>]+src="([^">]+)"' # только путь к картинке
# test_string = 'Картинка <img src="bg.jpg"> в тексте</p>'  # ['bg.jpg']
# result = re.findall(pattern, test_string)
# print(result)

# pattern = r'<p>(.*?)</p>' # без "?" выпадет <i>и т.д.</i>
# test_string = '<b>Вот начало: </b><p>Содержимое</p><i>и т.д.</i><p>документа</p>'  # ['Содержимое', 'документа']
# result = re.findall(pattern, test_string)
# print(result)

pattern = r'<p[^>]*>(.*?)</p>' # содержимое сайта с атрибутами align="center"
test_string = '<b>Центрируем</b><p align="center">Содержимое</p>'
result = re.findall(pattern, test_string)
print(result)