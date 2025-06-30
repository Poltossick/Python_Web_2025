# # startswith and endswith
# word = 'смотреть'
# if word.lower().startswith('см'): # if word[0] == 'c'
#     print('Да')
# if word.lower().endswith('ть'): # if word[-1] == 'ь'
#     print('yes')
from itertools import count
from turtledemo.penrose import start

# # find
# phrase = 'смотреть, видеть, вертеть'
# index = phrase.find('еть')  # возвращает первое упоминание, ищем с начала строки phrase
# index_3 = phrase.find('еть', 8)  # поиск второго вхождения
# index_4 = phrase.find('и', 8, 15)  # поиск в диапазоне
# index_2 = phrase.find('Ъ') # проверяет наличие, если -1, то этого нет
# print(index_4)

# word = 'синхрофазотрон'
# index = word.find('о')
# index_next = word.find('о', (index + 1))
# index_end = word.find('о', (index_next +1))
# print('Сколько раз встречается буква "о":', word.count('о'), 'раза.',
#       f' \nБуква "о" стоит на местах: {index}, {index_next}, {index_end}')

# word = 'синхрофазотрон'
# ch = 'о'
# numbers = set()
# if ch in word:
#     count = word.count(ch)
#     print(f'Буква \'{ch}\' встречается в слове \'{word}\' {count} раз(а)')
#     start = 0
#     for i in range(count):
#         pos = word.find(ch, start)
#         start = pos + 1
#         print(pos, end='\n')

# # replace
# word = 'тиливизор'
# print(word.replace('и', 'е'))
# print(word.replace('и', 'е', 2))

phone = '+7-012-345-67-89' # => +7 (012) 345-67-89
res = phone.replace('-', ' (', 1)
res = res.replace('-', ') ', 1)
print(res)
print(phone.replace('-', ' (', 1).replace('-', ') ', 1))