a = 3
b = 5

print('До: ')
print('a=', a, 'b=', b)

a, b = b, a #swap
"""
temp = a
a = b
b = temp 
"""

print('После: ')
print('a=', a, 'b=', b)