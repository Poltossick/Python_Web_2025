
lst = []
while (ingredients := input('Введите ингридиент: ')) != '': # - создаем список
    lst.append(ingredients)
temp = set(lst)  # чтобы убрать повторы
lst = list(temp)  # чтобы убрать повторы
print(f'Всего {len(lst)} ингредиентов: ')

lst.sort()
for name in range(len(lst)):
    print(str(name + 1) + '.', lst[name])