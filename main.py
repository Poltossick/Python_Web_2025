print(f'Возможные ходы:\n\tL - влево\n\tR - вправо\n\tF - прямо\n\tQ - выход')
flag = True
while flag:
    ch = input('Ваш выбор: ')
    match ch:
        case 'L' | 'l' | 'д' | 'Д' :
            print('Свернули налево')
        case 'R' :
            print('Свернули направо')
        case 'F':
            print('Пошли прямо')
        case 'Q' | 'q' | 'Й' | 'й' :
            print('выход в меню')
            flag = False
        case _:
            print('выбор не ясен')