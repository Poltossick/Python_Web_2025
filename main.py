# flag = True
# while flag:
#     height = int(input('Введите рост: '))
#     if 165 < height < 180:
#         print('Вы проходите')
#         flag = not flag
#     else:
#         print('Вы не проходите')

height = int(input('Введите рост: '))
while not (165 < height < 180):
    print('Вы не проходите')
    height = int(input('Введите рост: '))
print('Вы проходите')