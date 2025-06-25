# a = 123456.4
# lenght = len(str(a))
# print (lenght)

# word = input('Введите слово из 4 букв: ')
# if not word or len(word) != 4:
#     print('Неверный формат слова')
# if len(word) == 4:
#     print('Верно')
# else:
#     print('Попробуйте снова')

word = input('Введите слово дл анализа длины: ')
if not word or len(word) < 4:
    print('Попробуйте снова')
else:
    print('Длина слова "'+ word +'" =', len(word))