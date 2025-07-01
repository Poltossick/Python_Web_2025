# Словари (dictionary)

dic = {
    1: 'one',
    2: 'two',
    3: 'three',
    (55.75, 37.5): 'Москва'
}
print('0 ', dic[(55.75, 37.5)])

# перебор по умолчанию
for key in dic:
    print('1 ', key, 'переводится как ', dic[key])
# список ключей
print('2 ', dic.keys()) # список ключей
print('3 ', list(dic.keys()))
print('4 ', dic.values()) # список значений
print('5 ', list(dic.values()))

for value in dic.values():
    print('6 ', value)

print('7 ', dic.items()) # перебор пар ключ = значение
for k, v in dic.items():
    print('8 ', k, '=', v)

if 'two' in dic.values(): # поиск по значению
    print('9  Да, есть')
# dir({})
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__',
#  '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print('10  Доступ к несуществующему ключу без "исключений"')
pear = dic.get(4, 'не добавили') # второй параметр = значение по дефолту
print('10  Где 4:', pear)
