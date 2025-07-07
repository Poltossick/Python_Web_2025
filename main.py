# Пишем и подключаем свои модули

from package_test import greet, add  # -> из разных файлов Python загрузились через один пакет

print(greet('Мир!'))
print(add(3, 5, 0))

# from package_test.module import _hidden_function # '_' перед наименованием функции
# # означает ее закрытость от внешнего пользования
# print(_hidden_function())
