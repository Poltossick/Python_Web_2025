# Функция с переменным числом аргументов


# def multiply(first, *args):
#     """
#
#     :param first: постоянная, обязательно должна быть
#     :param args: переменная
#     :return:
#     """
#     if not args:
#         return first
#     result = first
#     for arg in args:
#         result *= arg
#     return result
#
#
# print(multiply(2, 3, 4, 5))  # 120
#
#
# def multy(*args, first):
#     if not args:
#         return first
#     result = first
#     for arg in args:
#         result *= arg
#     return result
#
#
# print(multy(2, 3, 4, first=5))  # 120
#
#
# def fio(name, surname):
#     return f'{name} {surname}'
#
#
# print(fio('Остап', 'Бендер') == fio(surname='Бендер', name='Остап'))  # True


def calc(operator, *args):
    match operator:  # мэтч - с чем совпадет оператор
        case '+':  # в случае если
            res = 0
            for arg in args:
                res += arg
        case '*':  # в случае если
            res = 1
            for arg in args:
                res *= arg
        case _:  # случай по дефолту
            return -float('inf')
    return res


print(calc('*', 3, 3, 3))
