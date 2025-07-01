# Функции
# Return value = завершение работы функции

def square(num):
    return num ** 2

def even_odd(num):
    if num % 2 == 0:
        return 'четное'
    return 'нечетное'

def print_string(s=None):
    if s is None:
        return
    print(str)

temp = square(5)
print(temp)
print(even_odd(temp))
