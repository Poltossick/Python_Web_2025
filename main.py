from multiprocessing.pool import worker

# lst = []
# while (ingredients := input('Введите ингридиент: ')) != '': # - создаем список
#     lst.append(ingredients)
# temp = set(lst)  # чтобы убрать повторы
# lst = list(temp)  # чтобы убрать повторы
# print(f'Всего {len(lst)} ингредиентов: ')
#
# lst.sort()
# for name in range(len(lst)):
#     print(str(name + 1) + '.', lst[name])

# lst = []
# N = 5
# for name in range(N):
#     print(f'На стол положили книгу {str(name + 1)}')
#     lst.append(name)
# while lst:
#     item = lst.pop() # lst.pop(0) = очередь от первой книги
#     print(f'Со стола берем книгу {item + 1}')

    # Создание аббревиатур
    # курсы
    # повышения
    # квалификации
    # КПК
lst = []
while (word := input('Введите слово: ').strip()) != '':
    lst.append(word[0].upper()) # добавляем только 1 букву из введенного слова
print(*lst, sep='') # " * " -- множество аргументов