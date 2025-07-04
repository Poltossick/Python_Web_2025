# Работа с изображением - растровое изображение
# thumbnail - скрипт на уменьшение изображения для публикации на сайте микро-изображения
from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (600, 400), (0, 0, 255))  # -> создание холста

POLY = [(50, 50), (150, 50), (50, 150)]

draw = ImageDraw.Draw(image)
draw.rectangle((10, 10, 590, 390), fill=(0, 192, 192), outline=(255, 255, 255), width=10)
draw.ellipse((15, 15, 585, 385), fill=(180, 170, 180), outline=(0, 0, 0), width=10)
draw.line((0, 0, 600, 400), fill=(15, 150, 0), width=5)
draw.line((0, 400, 600, 0), fill=(150, 15, 0), width=5)
draw.polygon(POLY, outline='white', width=12)
draw.text((100, 100), 'Hello, word', fill=(0, 0, 0), font_size=66)

image.save('./images/blue.jpg')
