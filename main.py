# Задача 1

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# loop = True
# while loop:
#     try:
#         index = int(input('Введите индекс: '))
#         print(f'Число по индексу {index}: {lst[index]}')
#     except ValueError:
#         print('Индекс вне диапазона')
#     except IndexError:
#         print('Индекс от 0 до 8 включительно')
#     # except Exception as exp:
#     #     print('Ошибка', exp.__class__.__name__, ':', exp)
#     else:
#         loop = False

# Задача 2
# while True:
#     a = input('Введите первое число: ')
#     b = input('Введите второе число: ')

# while True:
#     a = input('Введите первое число: ')
#     b = input('Введите второе число: ')
#     try:
#         if not int(b) != 0:
#             raise ZeroDivisionError ('На ноль делить нельзя')
#         else:
#             print('Ответ:', int(a) / int(b))
#             break
#     except ZeroDivisionError as expt:
#         print(expt)
#     except ValueError:
#         print('Должно быть число')

while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    try:
        res = int(a) / int(b)
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except ValueError:
        print('Должно быть число')
    else:
        print('Ответ:', res)
        break



