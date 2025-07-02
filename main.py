# Оператор is - проверяем сравнение ID объекта (его адрес)
# == - сравнивает содержимое, наполняемость объектов

# a = 1
# print(id(a))
# a += 1
# print(id(a))
#
#
# b = [0]
# print(id(b))
# b[0] += 1
# print(id(b))
#
#
# c = {'c': 0}
# print(id(c))
# c['c'] += 1
# print(id(c))

# my_ref = ['колбаса', 'сыр', 'масло']
# his_ref = ['колбаса', 'сыр', 'масло']
# print(my_ref == his_ref)  # содержимое одинаково True
# print(id(my_ref) == id(his_ref))  # два разных объекта False
#
# her_ref = my_ref
# print(my_ref == her_ref)  # ссылка на один объект True
# print(id(my_ref) == id(her_ref))  # ссылка на один объект True
# print(my_ref is her_ref) # ссылка на один объект True
#
# your_ref = my_ref.copy()
# print(my_ref == your_ref)  # содержимое одинаково True (полная копия)
# print(id(my_ref) == id(your_ref))  # два разных объекта False

# temp = None
# print(type(temp)) # <class 'NoneType'>
# print(temp is None) # True
# if temp is None: # нельзя писать temp == None
#     pass


# Функция выводит массив
def print_array(array: list, start: int = None):
    if start is not None and start > len(array):
        return
    if start is None:
        start = 0
    for item in range(start, len(array)):
            print(array[item])


a = [1, 2, 3]
print_array(a, 5)
