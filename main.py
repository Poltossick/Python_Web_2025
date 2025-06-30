#
# channels = ['red', 'greed', 'blue'] # == ('red', 'greed', 'blue')
# # r, *g = channels # распаковка
# # количество элементов должно быть равно количеству переменных, если меньше, написать ' * ' перед последним
# a, b, c = channels # распаковка
# print(b)

# a, b ,c = input('введите a: '), input('введите b: '), input('введите c: ')
# print(a, b, c)

# channels = [128, 200, 155]
# r, g, b = channels
# print(r, g, b)

N = 3
tpl = []
for _ in range(N):
    a, b = input('Введите фамилию: ').title(), float(input('Введите средний балл: '))
    tpl.append((a, b))
    # tpl.sort()
print(tpl)
for name in tpl:
    a, b = name
    print(f'Студент: {a}. Средний бал: {b}')
