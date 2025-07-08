# Исключения - (runtime - время исполнения программы) except
# print(name) # -> NameError: name 'name' is not defined
# file_object = open('information.txt') # -> FileNotFoundError: [Errno 2] No such file or directory: 'information.txt'
# try:
#     file_object = open('information.txt', encoding='utf-8')
# except FileNotFoundError:
#     print('Файл не найден. Файл создан с параметрами по умолчанию')
#     with open('information.txt', 'wt', encoding='utf-8') as file_object:
#         file_object.write('По умолчанию')
# else:
#     print('Файл открыт успешно. Читаем его и закрываем.')
#     print('Текст в файле: ', file_object.read())
#     file_object.close()
# finally:
#     print('Продолжаем работать.')

flag = False
try:
    file_object = open('information.txt', encoding='utf-8')
except FileNotFoundError:
    file_object = open('information.txt', 'wt', encoding='utf-8')
    flag = True
    print('Файл не найден. Файл создан с параметрами по умолчанию')
else:
    print('Файл открыт успешно. Читаем его и закрываем.')
    print('Текст в файле: ', file_object.read())
    file_object.close()
finally:
    if flag:
        file_object.write('По умолчанию')
        file_object.close()
    print('Продолжаем работать.')
