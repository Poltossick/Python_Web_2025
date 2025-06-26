num = 3 # число которое нужно угадать
flag = True # изменяет значение по событию
var = ''
print('угадай число')
while flag:
    var = int(input('Ваш вриант: '))
    if var == num:
        print('Молодец')
        flag = not flag # флаг инвертирован, аналогичной flag = False
    elif var > num:
        print('число меньше')
    else:
        print('число больше')
print('Конец')