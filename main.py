# Работа с изображением - растровое изображение
# thumbnail - скрипт на уменьшение изображения для публикации на сайте микро-изображения
from PIL import Image

img = Image.open('images/python.jpg')

# print(img.size) # -> свойство возвращает картеж (800, 600)
x, y = img.size  # -> x (w) -- ширина (с лева на право), y (h) -- высота (сверху вниз)
# print('Ширина (х) - ', x, 'Высота (y)', y) # -> Ширина (х) -  800 Высота (y) 600
mode = img.mode
# print('Цветовая схема (mode) - ', mode) # -> свойство - Цветовая схема (mode) -  RGB


pixels = img.load()  # -> загрузить таблицу пикселей

# инверсия
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j] # -> обращение в виде картежа
#         pixels[i, j] = g, b, r

# негатив
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]  # -> обращение в виде картежа
#         pixels[i, j] = 255 - r, 255 - g, 255 - b

# Grayscale - оттенки серого - черно-белая картинка
# (0,0,0) - (1,1,1) - (245,245,245)
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]  # -> обращение в виде картежа
#         average = (r + g + b) // 3
#         pixels[i, j] = average, average, average
img.save('images/python2.jpg')


img.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save('images/python_FLIP_LEFT_RIGHT.jpg')
img.transpose(Image.Transpose.FLIP_TOP_BOTTOM).save('images/python_TOP_BOTTOM.jpg')
img.rotate(30).save('images/python_rotated.jpg')
img.crop((250, 0, 550, 200)).save('images/python_cropped.jpg')
img.resize((400, 300)).save('images/python_resized.jpg')

