import random
from random import random, randrange, randint, choice

print('Определение фальшивой монеты')
a = choice(range(50))
b = choice(range(50))
c = choice(range(50))
print(f'a = {a},\nb = {b},\nc = {c}')
if a == b:
    print(f'{a} равно {b}\n\t с - фальшивая монета')
elif a != b and a > b:
    print(f'{a} не равно {b} и {a} больше {b}\n\tb - фальшивая монета')
elif a != b and a < b:
    print(f'{a} не равно {b} и {a} меньше {b}\n\ta - фальшивая монета')
else:
    print('нет решения')
print('задача решена')

