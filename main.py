# Функция, как объект
# передается в другие функции -> функции высшего порядка

# печатник = print
# печатник(2+3)

# Функция критерия отбора элементов списка

def is_longer_six(word):
    """
    Критерий: длина слова / строки
    :param word: список слов
    :return: слова от 7 букв и больше
    """
    # if len(word) > 6:
    #     return True
    # return False
    return len(word) > 6

words = ['в','списке', 'останутся', 'слова', 'длина', 'которых',
         'больше', 'шести']
res = list(filter(is_longer_six, words)) # отфильтровали список по функции
print(res)

for word in filter(is_longer_six, words):
    print(word)


def is_letter_a(word):
    """
    Критерий: первая буква А
    :param word: список слов
    :return: слова на А
    """
    return word[0] == 'а'

fruits = ['арбуз', 'ананас', 'банан', 'груша']
for word in filter(is_letter_a, fruits):
    print(word)