from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

orig = Image.open('images/python.jpg')
# размытие
# blur_img = orig.filter(ImageFilter.GaussianBlur(radius=5))
# blur_img.show()

# резкость
# enhance_img = ImageEnhance.Sharpness(orig)
# sharpened_img = enhance_img.enhance(50.0)
# sharpened_img.show()

#получить контуры
edges = orig.filter(ImageFilter.FIND_EDGES)
edges.show()

# orig = Image.open('images/sunny_day.jpg').convert('RGB')
#
# up = orig.crop((0,0,600,200))
# down = orig.crop((0,200,60,400))
# new = Image.new('RGB', (600,400))
#
# new.paste(down, (0,0))
# new.paste(up, (0, 200))
#
# new.show()

# # https://fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru
# W = 600
# H = 400
#
# image = Image.new('RGB',
#                   (W, H),
#                   (0, 163, 232))
#
# draw = ImageDraw.Draw(image)
#
# text = 'Солнечный день'
# # draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
# draw.circle((600, 0), 100, fill='yellow')
# font = ImageFont.truetype(
#     # font='arial.ttf',  # можно использовать любой установленный шрифт
#     font='fonts/Geisha.ttf',
#     size=50
# )
# # Получаем размеры текста
# _, _, w, h = draw.textbbox((0, 0), text, font=font)
#
# # Рассчитываем позицию для центрирования
# x = (W - w) // 2
# y = (H - h) // 2
#
# draw.text((x, y), text, fill=(255, 255, 0), font=font)
#
# image.save('images/sunny_day.jpg')
# # image.show()