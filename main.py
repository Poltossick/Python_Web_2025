N = 5
total = 0
min_val = float('inf')  # + бесконечность
max_val = float('-inf')  # - бесконечность
prod = 1
for _ in range(N):
    num = int(input('Введите целое число: '))
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    total += num
    ave = total / N
    prod *= num
print('Сумма =', total)
print('Среднее арифметическое =', ave)
print('минимум =', min_val)
print('максимум =', max_val)
print('произведение =', prod)
