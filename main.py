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

# print('Остаток от деления: ')
# loop = True # цикл
# while loop:
#     try:
#         value = int(input('На что делим число 10: '))
#         res = 10 % value
#         print(f'остаток от деления 10 на {value} = {res}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#     # except ValueError:
#     #     print('Надо вводить только целые числа')
#     except Exception as exp:
#         print('Произошло исключение: ', exp.__class__.__name__, ' - ', exp)
#     else:
#         loop = False

#  'Бросаемся' исключениями - raise (throw в других языках)
max_val = 10
min_val = 1
loop = True # цикл
while loop:
    try:
        val = int(input(f'Введите целое число от {min_val} до {max_val}: '))
        if not min_val < val < max_val:
            raise ValueError('введенное число вне диапазона')
        print(f'Введенное число {val} лежит в заданном диапазоне')
    except ValueError as exp:
        print('Надо быть внимательнее:', exp)
    else:
        loop = False