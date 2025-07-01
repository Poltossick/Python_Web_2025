# списочное выражение (list comprehension)

# # список квадратов чисел
# squares = []
# for i in range(10):
#     squares.append(i ** 2)
# print(*squares, sep=', ')
#
# squares_1 = [i ** 2 for i in range(10)] # оптимальный способ написания
# print(*squares_1, sep=', ')
#
# # список квадратов четных чисел
# squares_2 = [i ** 2 for i in range(10) if i % 2 == 0] # оптимальный способ написания
# print(*squares_2, sep='-')
# row = [a for a in range(1, 3)]
# print(row)

# # произведение i и j
# for i in range(3):
#     for j in range(3):
#         print([i * j], end=', ')
# print(f'\n{[i * j for i in range(3) for j in range(3)]}')
#
# num = '500 600 700 800'
# a = [int(item) for item in num.split()]  # присвоить переменной для каких-либо действий
# print(a)
# approved = ['500', '800']
# print([int(item) for item in num.split() if item in approved])
# approved_1 = [500, 800]
# print([int(item) for item in num.split() if int(item) in approved_1])

# задача
text = 'Списочные выражения иногда применяются для конкретно эффективности кода программы'
print([item for item in text.split()[2::3]]) # операции со списком