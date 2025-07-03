ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
# print(ENGLISH_ABC)
RUSSIAN_ABC = [chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё']
# print(RUSSIAN_ABC)
ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^
       set([x.upper() for x in ENGLISH_ABC]) ^
       set([x.upper() for x in RUSSIAN_ABC]))
print(ABC)

text = 'В Индии семерых инженеров уволили после постройки моста с 90-градусным поворотом.'
res = ''.join(filter(lambda x: x in ABC ^ {' '}, text))  # -> удаление знаков препинания
print(res)


def remove_punctuation(txt):
    """
    Функция удаления знаков препинания
    :param txt: исходный текст
    :return: текст без знаков препинания
    """
    return ''.join(filter(lambda x: x in ABC ^ {' '}, text))


def get_words(txt):
    """
    Функция вывода текста списком
    :param txt: функция удаления знаков препинания
    :return: текст списком
    """
    return remove_punctuation(txt).split()


def long_words(txt, lenght=4):
    """
    Фильтр слов по длине 4
    :param txt: функция вывода текста списком
    :param lenght: длина слова
    :return: список слов по длине 4
    """
    return list(filter(lambda word: len(word) >= lenght, get_words(txt)))


print(long_words(text))

