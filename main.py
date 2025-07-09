# Регулярные выражения (поиск по паттерну)
# Regular Expression - папка при написании "re"
# r-строка — raw-string (сырая строка)
import re
import requests

pattern = r'<img[^>]+src="([^">]+)"'
# test_string = '<img height="50" width="150" src="./images/bg.jpg">'
html = requests.get('https://skillbox.ru').text
# print(html)
result = re.findall(pattern,html)
print(result)
