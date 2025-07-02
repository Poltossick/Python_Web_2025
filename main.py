# args (arguments) and kwargs (keyword arguments пишется как имя=значение)
# def print_any(*args, **kwargs):
#     for item in args:
#         print(item)
#     for k, v in kwargs.items():
#         print(k, '=', v)
#
#
# print_any('Petr', 'Filatov', city='Moscow', age=27)

def profile(name, surname, city, *children, **additional):
    print(f'Имя = {name}')
    print(f'Фамилия = {surname}')
    print(f'Город = {city}')
    if len(children) > 0:
        print(f'Дети: {', '.join(children)}')
    if 'hobby' in additional:
        print('Хобби:', ', '.join(additional['hobby']))



profile('Михаил', 'Филатов', 'Абакан', 'Мария', 'Иван',
        hobby=['Тенис', 'Плавание'])