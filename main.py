# ОС-модуль - работа с операционной системой

file_obj = open('info.txt', 'rt', encoding='utf-8')
res = []
while temp := file_obj.readline().rstrip('\n'):
    res += temp.split(', ')
res = sorted(int(x) for x in set(res))

print(res)

file_obj.close()


file_obj = open('info.txt', 'rt', encoding='utf-8')

print(file_obj.readlines())

file_obj.close()