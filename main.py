# Декораторы


def upper_case_print(old_function):
    def new_function(*args, **kwargs):
        args_up_case = [str(arg).upper() for arg in args]
        old_function(*args_up_case, **kwargs)
    return new_function

new_print = upper_case_print(print)
new_print('привет андрей')


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