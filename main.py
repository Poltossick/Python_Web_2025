# Функция с переменным числом аргументов

def multy(*args):
    print(len(args)) # подсчет числа аргументов = 2
    print(args) # обращение к каждому аргументу по индексу либо перебором в цикле = (1, 3)

multy(1, 3)

def multiply(*args):
    if not args:
        return 0
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply()) # args empty = return 0
print(multiply(3, 5)) #  15 = ((1 * 3) * 5)