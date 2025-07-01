# Словари (dictionary)
# # пустой словарь
# dic = {}
# dic_1 = dict()
# # предзаполненный словарь
dic = {
    'table': ['таблица', 'стол'],
    'well': ['хорошо', 'колодец', 'скважина'],
    'chair': 'стул',
    'apple': 'яблоко',
    1: 'один',
    'plum': ['слива'],
    }
# # print(dic['table'], dic[1], dic['well'][1], sep='\n')
# # dic['plum'].append('тест')
# # print(dic['plum'])
# del dic['table']
# print(dic) # словарь целиком, "как есть"
# for key in dic:
#     print(key, 'переводится как ', dic[key])

"""dir({}) - методы словаря
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__',
#  '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'] """

deleted_item = dic.pop(1)
print(deleted_item)

if 'chair' in dic: # поиск по ключу
    print('Стул есть')