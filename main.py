# Функции
# позволяют реализовать принцип сухого (DRY - dont repeat yourself)
# СИНТАКСИС :
# def <имя функции>([параметры]):
#     команды
#     команды по очереди относящиеся к функции
# 1-ый отступ по рер8
# 2-ой отступ по рер8
# <имя функции>('аргумент') -- вызов функции

person = 'Max' # input('Введите имя: ') # scope(global) глобальная перемена
count = 0 # scope(global) глобальная перемена

def greet(name='user'): # scope(local) - локальная переменная    print('Привет, ', name)
    print('Hello,', name)
    print(count)

def increment():
    global count # для воздействия на глобальную переменную
    count += 1

def print_list(array):
    for item in array:
        print(item)

greet()
greet(person)
increment()# меняет глобальную переменную после вызова функции
print_list(['meow', 'woof'])
