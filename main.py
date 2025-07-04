# result = sum(1, 2, 3) - ошибка, только итерируемый объект
lst = [1, 2, 3]
res = 0
for x in lst:
    res += x
print(res)
result = sum(lst)
min_v = min(lst)
max_v = max(lst)
print(result, min_v, max_v)