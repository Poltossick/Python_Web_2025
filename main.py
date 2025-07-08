# Практикум (обучаемый словарь)
import pickle

# минимальная выерсия, если файл dict.dat отсутствует
vocabulary = {
    'стол': 'table',
    'стул': 'chair',
}

def print_voc():
    """
    Функция для распечатки словаря
    :return: выводит словарь
    """
    print('Сейчас словарь содержит: ')
    for k, v in vocabulary.items():
        print(k, '—', v) # -> — Alt + 0151



try:
    with open('dict.dat', 'rb') as dump_in:
        vocabulary = pickle.load(dump_in)
        print_voc()
except FileNotFoundError:
    with open('dict.dat', 'wb') as dump_out:
        pickle.dump(vocabulary, dump_out)
    print('Создан минимальный словарь: ')
    print_voc()


while True:
    word = input('\nВведите слово для перевода или # для завершения: ').strip().lower()
    if word == '#' or word == '№':
        break
    if word in vocabulary.keys():
        translate = vocabulary[word]
        print(f'Слово "{word}" переводится как "{translate}".\n')
    else:
        print(f'Значение слова "{word}" отсутствует в словаре.\n')
        new_key = f'А как слово "{word}" переводится.  \n'
        new_key += f'Если ничего не вводите нажмите ENTER, \n'
        new_key += f'или введите его здесь: '
        new_word = input(new_key)

        if new_word != '' or len(new_word) > 1:
            vocabulary[word] = new_word
            print(f'Слово "{word}" с переводом "{new_word}" внесено в словарь.')
        else:
            print('Ничего не введено или слишком короткое слово')
            continue

with open('dict.dat', 'wb') as dump_out:
    pickle.dump(vocabulary, dump_out)

print('До новых встреч!')