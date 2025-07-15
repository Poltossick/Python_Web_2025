# Декораторы

def outer():
    x = 5
    def inner():
        nonlocal x
        print('Nonlocal x=', x)
        x = 10
    inner()
    print('New x=', x)

outer()

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
