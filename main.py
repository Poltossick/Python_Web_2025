# Файлы
# t - текстовые файлы (txt, html, xml)
# b - бинарный файлы (jpg, avi, mp3)
# w - write (запись файла, создается) - открывается очищенный файл
# a - append (если не существует - создается, если существует - открывается весь с последними изменениями)
# r - read (файл должен существовать, открывается ТОЛЬКО на прочтение) - по умолчанию

# file_object = open('info.txt', 'wt', encoding='utf-8') # открывает файл
# # print(file_object.mode)
# # print(file_object.name)
# # print(file_object.encoding) -> encoding='utf-8'
#
# count = file_object.write('Этот текст будет в файле')
# print(f'В файл записан {count} байт!')
#
# file_object.close()

# file_obj = open('info.txt', 'rt', encoding='utf-8')
#
# text = file_obj.read(3)# -> в скобках пишется сколько байт читать
# file_obj.read(6+7)
# text += file_obj.read(8)
# print('Вот что было в файле' , end=': ')
# print(text)
#
# file_obj.close()

# file_obj = open('info.txt', 'at', encoding='utf-8')
# file_obj.write(f'\nЭто хороший текст!')
# file_obj.close()

# file_obj = open('info.txt', 'at', encoding='utf-8')
#
# print('\nА вот еще одна строка.', file=file_obj)
#
# file_obj.close()

# file_obj = open('info.txt', 'rt', encoding='utf-8')
#
# while text := file_obj.readline():
#     for line, str in enumerate(file_obj, 1):
#         print(f'{line}. {str.rstrip('\n')}')
#
#
# # lst = file_obj.readlines()
# # lst = list(map(lambda x: x.strip('\n'), lst))
# # print(lst)
#
# # text = file_obj.read()
# # lst = text.splitlines()
# # print(lst)
#
# file_obj.close()



# открытие с менеджером контекста, проследит, чтобы файл закрылся
with open('info.txt', 'rt', encoding='utf-8') as file_obj:
    while text := file_obj.readline():
        for line, str in enumerate(file_obj, 1):
            print(f'{line}. {str.rstrip('\n')}')

