min_val = float('inf')
max_val = float('-inf')
total = 0
total_suc = 0

while (num := int(input('Введите рост участника: '))) != -1:
    if 150 <= num <= 180:
        total_suc += 1
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    total += 1

print(f'Итого\n\tвсего = {total}\n\tпрошли успешно = {total_suc}'
f'\n\tминимальный рост = {min_val}\n\tмаксимальный рост = {max_val}')
