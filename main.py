# словарные выражения -> dict comprehensive

# ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# # print(ENGLISH_ABC)
# RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
# # print(RUSSIAN_ABC)
# ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^
#        set([x.upper() for x in ENGLISH_ABC]) ^
#        set([x.upper() for x in RUSSIAN_ABC]))
# news = 'В Индии семерых инженеров уволили после постройки моста с 90-градусным поворотом.'
#
# res = ''.join(filter(lambda x: x in ABC ^ {' '}, news))  # -> удаление знаков препинания
#
#
# def remove_punctuation(txt):
#     """
#     Функция удаления знаков препинания
#     :param txt: исходный текст
#     :return: текст без знаков препинания
#     """
#     return ''.join(filter(lambda x: x in ABC ^ {' '}, news))
#
#
# def get_words(txt):
#     """
#     Функция вывода текста списком
#     :param txt: функция удаления знаков препинания
#     :return: текст списком
#     """
#     return remove_punctuation(txt).split()
#
#
# def long_words(txt, lenght=4):
#     """
#     Фильтр слов по длине 4
#     :param txt: функция вывода текста списком
#     :param lenght: длина слова
#     :return: список слов по длине 4
#     """
#
#     return list(filter(lambda word: len(word) >= lenght, get_words(txt)))
#
#
# fruits = ['банан', 'яблоко', 'ананас', 'арбуз', 'малина', 'киви', 'ява']
# print(sorted(fruits, key=lambda x: len(x)))  # -> ['ява', 'киви', 'банан', 'арбуз', 'яблоко', 'ананас', 'малина']
# print(sorted(fruits, key=lambda x: x[-1]))  # -> ['малина', 'ява', 'арбуз', 'киви', 'банан', 'яблоко', 'ананас']
# print(sorted(fruits, key=lambda x: (x[-1], len(x))))
# # -> ['ява', 'малина', 'арбуз', 'киви', 'банан', 'яблоко', 'ананас']
#
#
# news = 'Я знаю, что я ничего не знаю. Другие не знают даже этого, а значит - я знаю больше них.'
# d = {}
# text = get_words(news)
#
# for word in text:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1
#
# res = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
# for k, v in res.items():
#     print(k, v)

goods = [
    ['утюг', 1000, 2],
    ['фен', 1000, 5],
    ['фартук', 1000, 5],
    ['форма', 1000, 1],
    ['фокус', 1000, 3],
    ['телевизор', 8000, 3]
]

# Sorted = всегда выводит отсортированный список
print(sorted(goods, key=lambda s: (s[1], s[2], s[0]))) # сортировка по цене, по количеству, по алфавиту
# -> [['форма', 1000, 1], ['утюг', 1000, 2],
# ['фокус', 1000, 3], ['фартук', 1000, 5], ['фен', 1000, 5], ['телевизор', 8000, 3]]