# # Методы строки split() и join()
# text = 'один два три четыре'
# lst = text.split() # по умолчанию берет в качестве разделителя все символы пустого пространства
# print(lst)
# ip = '192.168.0.1'
# lst = ip.split('.')
# print(lst)
#
# #['192', '168', '0', '1']
# text2 = '-'.join(lst) # соединительный элемент ставится перед join
# print(text2)

text = '  P   y t h o     n    '
# temp = text.split()
# res = ''.join(temp)
result = ''.join(text.split()) # убрать все пробелы
print(result)