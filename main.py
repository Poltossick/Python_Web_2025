flag = True
while flag:
    high = int(input('Введите рост: '))
    if high > 165 and high < 180:
        print('Вы проходите')
        flag = not flag
    else:
        print('Вы не проходите')
