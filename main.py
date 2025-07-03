# словарные выражения -> dict comprehensive

numbers = range(1, 11)
squares = {n: n ** 2 for n in numbers if n % 2 == 0}
squares = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
print(squares)

sours_dict = {
    'x': 1,
    'y': 2,
    'z': 3,
}

dest_dict = {v ** 2 for v in sours_dict.values()}
print(dest_dict) # -> {1, 4, 9}
dest_dict = {k: v ** 2 for k, v in sours_dict.items()}
print(dest_dict) # -> {'x': 1, 'y': 4, 'z': 9}
