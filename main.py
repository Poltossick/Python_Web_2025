# проверка коллекций: any() & all()
# any() - любой элемент коллекции возвращает True / False
# all() - все элементы коллекции возвращает True / False

# print(all([1, 2, 3, -1])) # все элементы не нулевые true
# print(all([1, 2, 0])) # один элемент нулевой false
# print(all([])) # все элементы не нулевые true

words = 'один, два, три'.split()
# list_for_analyze = list(map(lambda x: len(x) > 3, words))
print(all(list(map(lambda x: len(x) > 3, words)))) # -> False
print(any(list(map(lambda x: len(x) > 3, words)))) # -> True