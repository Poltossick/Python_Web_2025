# ax + bx + c = 0
a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if a != 0:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('d =', (b ** 2 - 4 * a * c))
        print('Уравнение не имеет корней')
    elif d == 0:
        print('d =', (b ** 2 - 4 * a * c))
        print(f'Корень уравнения:\n\tx =', - b / 2 * a)
    elif d > 0:
        print('d =', (b ** 2 - 4 * a * c))
        print(f'Корни уравнениия:\n\tx1 =', round((- b + d ** (1 / 2)) / 2 * a, 2),
        f'\n\tx2 =', round((- b - d ** (1 / 2)) / 2 * a, 2))
else:
        print('"a" не может быт меньше нуля')
