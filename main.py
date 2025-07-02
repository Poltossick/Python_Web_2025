def sandwich(type_of_meal, with_onion=False, with_tomato=False):
    print('bread')
    if with_onion:
        print('onion')
    print(type_of_meal)
    if with_tomato:
        print('tomato')
    print('bread')


sandwich('chicken', with_onion=True, with_tomato=True)
