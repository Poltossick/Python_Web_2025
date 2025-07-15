# Декораторы

import time


def timeit(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        finish = time.time()
        print(f'Функция исполнялась: {finish - start:.4f} сек.')
        return result

    return wrapper

@timeit
def test():
    time.sleep(1.184856218)

test()


# def logger(function):
#     counter = 0
#     def decorated_function(*args, **kwargs):
#         nonlocal counter
#         counter +=1
#         print(counter, '->', 'Аргументы:', args,
#               'Именованные аргументы:', kwargs)
#         result = function(*args, **kwargs)
#         print('____', 'Результат:', result)
#     return decorated_function
#
# @logger
# def make_burger(meal='Chicken', onion=False, tomato=False):
#     print('Bread')
#     if onion:
#         print('Onion')
#     print(meal)
#     if tomato:
#         print('Tomato')
#     print('Bread')
#
# make_burger(onion=True, tomato=True)
# make_burger('Fish', tomato=True)


# def outer():
#     x = 5
#     def inner():
#         nonlocal x
#         print('Nonlocal x=', x)
#         x = 10
#     inner()
#     print('New x=', x)
#
# outer()

# def upper_case_print(old_function):
#     def new_function(*args, **kwargs):
#         case = kwargs.pop('case', None)
#         if case == 'U':
#             args = [str(arg).upper() for arg in args]
#         elif case == 'L':
#             args = [str(arg).lower() for arg in args]
#         return old_function(*args, **kwargs)
#     return new_function
#
#
# new_print = upper_case_print(print)
# new_print('Привет, Андрей')
# new_print('Привет, Андрей', case='U')
# new_print('Привет, Андрей', case='L')

# def answer(question):
#     return 'Думайте сами'
#
# def dialog():
#     def answer(question):
#         if question.lower().startswith('когда'):
#             return 'Никогда'
#         else:
#             return 'Упс'
#     question = input()
#     while question != '':
#         print(answer(question))
#         question = input()
#
# dialog()
