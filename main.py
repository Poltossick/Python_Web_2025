# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # -> 123456789
# res = ''.join(map(str, nums))
# print(res)

# Критерий вхождения подстроки
# в частности 'ан'
fruits = ['банан', 'ананас', 'арбуз', 'киви']
def string_contain(str):
    return 'ан' in str

print(string_contain('банан'))

res = list(filter(string_contain, fruits)) # -> ['банан', 'ананас']
print(res)

