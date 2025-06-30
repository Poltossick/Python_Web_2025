# # Кортеж tuple - неизменяемый список, который можно сразу задать
# # BLACK = (0, 0, 0) - пример
# empty = () # tuple()
# print(empty)
# s = 'Python'
# emp = tuple(s) + ('.', ) # объединение 2-х картежей в 3-й
# # чтобы создать кортеж из 1 знака, важно добавить запятую
# emp_1 = list(emp) # перевести в лист чтобы внести изменения в картеж
# emp_1[1] = 'И'
# print(*emp_1, sep='')

# print(dir(tuple))
# ['__add__', '__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

