abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # Д/з шифр цезаря, попробовать зациклить через меню
# подсказка остаток на деление в помощь
# print(dir(abc))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',  '__subclasshook__',

#  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
#  'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
#  'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
#  'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
#  'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
#  'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# phrase = 'Язык Phython. Привет'
# print(phrase.lower()) # все маленькие
# print(phrase.upper()) # все большие
# print(phrase.capitalize()) # первое слово с заглавной
# print(phrase.title()) # все слова с заглавной
# print('Ура ' * 3)
# print(phrase.count('y'))
# print(phrase.index('Я')+1)

word = 'статор'
res = ''
for item in range(len(word)):
    res += word[item]  * (item + 1)
    print(res)
for i in range(1, len(word) + 1):
    print(word[i - 1] * i, end=' ')