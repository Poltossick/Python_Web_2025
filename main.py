# Регулярные выражения (поиск по паттерну)
# Regular Expression - папка при написании "re"
# r-строка — raw-string (сырая строка)
import re

# def remove_punctuation(input_str: str) -> str:
#     """
#     Методом sub() заменяем все найденный совпадения пустой строкой
#     и возвращаем очищенную
#     :param input_str: строка со знаками препинания
#     :return: строку, очищенную от этих знаков препинания
#     """
#     return re.sub(r'[^\w\s]', '', input_str)
#
#
# test_string = 'Язык Python, явл?яясь инту"итивно понятным, пр,ост для изучения! Ну и PEP8/'
# result = remove_punctuation(test_string)
# print(result)

# pattern = r'[^\w\s]'
# test_string = 'яблоко,груша;банан!абрикос?слива'
# result = re.split(pattern, test_string)
# print(result)

# pattern = r'[,:;!?.]'
# test_string = 'яблоко,   груша;   банан!   абрикос?   слива  '
# result = re.split(pattern, test_string)
# print(''.join(result).split())  # -> ['яблоко', 'груша', 'банан', 'абрикос', 'слива']
# print((list(map(lambda x: x.strip(), result))))  # через функцию map и lambda
# print([x.strip() for x in result])  # списочное выражение

