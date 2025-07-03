# анонимные функции (безымянные, однострочные)
# lambda-функции
# lambda <аргумент>: <выражение>
# lambda <arg>: <return>

is_longer_six = lambda word: len(word) > 6
is_first_letter_a = lambda word: word[0] == 'c'
is_string_contains = lambda s: 'ст' in s

words = ['в','списке', 'останутся', 'слова', 'длина', 'которых',
         'больше', 'шести']
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# res = list(filter(lambda word: word[0] == 'с', words)) # -> ['списке', 'слова']
# print(res)
#
# res = list(filter(lambda word: len(word) > 6, words)) # -> ['останутся', 'которых']
# print(res)
#
# res = list(filter(lambda s: 'ст' in s, words)) # -> ['останутся', 'шести']
# print(res)

res = list(map(lambda num: num ** 2, (range(3, 16)))) # -> [9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
res_2 = [num ** 2 for num in range(3, 16)] # -> [9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
print(res)

long_words = [len(word) > 6 for word in words] # -> выводит true and false
long_words_2 = [word for word in words if len(word) > 6]  # -> ['останутся', 'которых']
print(long_words_2)