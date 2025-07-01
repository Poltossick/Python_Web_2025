# вложенные списки (nested lists)
# array = массив[1, 38.6, True, 'cort', (1, 2)]
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# # обход двухмерного списка или матрицы
# for a in range(len(matrix)): # row = строки = сначала берет строки
#     for b in range(len(matrix[a])): # col = столбцы = второй раз берет столбец
#         print(matrix[a][b])

# симметричная матрица = строки = столбцы (N)
N = 3
count = 1
matrix = [[1] * N for _ in range(N)]
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        matrix[row][col] = count
        count += 1
print(matrix)

N = 3
count = 1
matrix = []
for row in range(N):
    table = []
    for col in range(count, count + N):
        table.append(col)
    matrix.append(table)
    count += N
print(matrix)

matrix = [[i + j for j in range(3)] for i in range(1, 10, 3)]
print(matrix)
