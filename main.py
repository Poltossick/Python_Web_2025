# # Игра города
# name = set()
#
# while (city := input('Назовите город ')) != 'не знаю':
#     if city in name:
#         print('Такой город уже был')
#     else:
#         name.add(city)
# print('Итого названо', len(name), 'городов')
# for item in name:
#     print('\t', item)

# Карты
cards = {'тройка', 'семерка', 'валет', 'дама', 'туз'}
while cards: # пока карты в колоде есть
    print(cards.pop())