# # Список (list)
# # lst = [] # - пустой список
# # lst = list() # - пустой список
# print(list(range(1,4)))
# lst = [1, 2, 3] * 2
# print(lst)
# lst_2 = list('Python')
# print(lst_2)
# print(type(lst_2)) # класс
# lst = [1, 2, 3]
# print(lst[2]) # индекс
# print(lst[:2]) # срез
from os import remove

# dir([])
# ['__add__', '__class__', '__class_getitem__', '__contains__',
#  '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__',
#  '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
#  '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
#  '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'append' (добавить вместо add), 'clear', 'copy', 'count' (сколько раз элемент в списке), 'extend',
#  'index' (как в строке), 'insert', 'pop', 'remove', 'reverse', 'sort']

# word = 'малоко'
# lst = list(word)
# lst[1] = 'о'
# print(lst)
#
# lst = [] # добавить [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] в пустой список
# for i in range(1, 11):
#     lst.append(i)
# print(lst)

# lst_1 = [1, 2, 3]
# lst_2 = [4, 5, 6]
# lst_2 += ['e']
# lst = lst_1 + lst_2 # сложить 2 списка
# print(lst)
# lst_2.extend(lst_1) # к одному из списков добавить другой список с конца
# print(lst_2)

# lst = list(range(10))
# # for item in lst:
# #     print(item, '-', item ** 2)
# sl = lst[::2]
# print(sl)
# for item in range(0, len(lst), 2):
#     print(lst[item], '-', lst[item] ** 2)

# lst = [1, 1, 1, 2, 3, 4, 5]
# del lst[::2]
# print(lst)
# lst.remove(1) #remove(value, /) method of builtins.list instance
#     Remove first occurrence of value. -- удаляет только первое конкретное вхождение
# print(lst)
# lst.pop()  # pop(index=-1, /) method of builtins.list instance
# #    Remove and return item at index (default last). -- удаляет по индексу
# print(lst)

# lst = [2, 5, 7 , 6 , 1, 3, 4]
# lst.sort()
# print(lst)
#
# lst.sort(reverse=True)
# print(lst)

a = ['a', 'b', 'c']
# b = a # не создает новый список, а ссылается на список а
b = a.copy()  # для создания нового списка вторая запись b = a[:] - запишите в b полный срез от а
b.append('d')  # b += ['d']
print(id(a))
print(id(b))
print(a)
print(b)
