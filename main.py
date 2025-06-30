# slice - срез
# [начало(включительно):окончание(не включительно):шаг]
# phrase = 'Добрый день'
# q = phrase.find('й') + 1
# print(phrase[3:9:]) # от n до m (не включая = 8)
# print(phrase[7:]) # от текущего индекса и до конца
# print(q)
# print(phrase[:q]) # от начала и до заданного индекса
# print(phrase[:-6])
# print(phrase[::2]) # от начала до конца с шагом 2
# print(phrase[::-1]) # инверсия, запись наоборот


# word = input('Введите слово: ').strip() # потоп
# word.replace(' ', '')
# if word.lower() == word.lower()[::-1]:
#     print('Строка является палиндромом')
# else:
#     print('Строка не является палиндромом')
#
# phrase = 'Дорог Рим' # Город Миргород
# print(phrase[:5:][::-1].lower().title(), phrase[::-1].replace(' ', '').lower().title())
# temp = phrase.lower()
# city = temp[:5][::-1]
# res = city + ' ' + temp[6:][::-1] + city
# print(res.title())
