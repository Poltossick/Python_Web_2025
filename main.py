# Работа с изображением - растровое изображение
# thumbnail - скрипт на уменьшение изображения для публикации на сайте микро-изображения
from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (600, 400), (0, 191, 255))  # -> создание холста

POLY = [(50, 50), (150, 50), (50, 150)]

draw = ImageDraw.Draw(image)
draw.ellipse((500, -100, 700, 100), fill=(255, 255, 0), outline=(255, 255, 0), width=50)
draw.text((150, 150), 'Sunny day', fill=(255, 255, 0), font_size=66)

image.save('./images/DAY.jpg')
