# Функция, как объект
# передается в другие функции -> функции высшего порядка


def square(num):
    return str(num)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = ''.join(list(map(square, nums)))
print(squares)

