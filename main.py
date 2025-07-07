# ОС-модуль - работа с операционной системой

import os

# os.mkdir('libs') # -> создание директории
# os.makedirs('libs', exist_ok=True) # -> 'мягкое' создание директории, вместо  os.mkdir('libs')
# os.rmdir('libs')  # -> удаление директории
# print(os.path.exists('libs'))  # -> проверить наличие директории
# if os.path.exists('libs'):
#     os.rmdir('libs')  # -> 'мягкое' удаление директории

path = os.getcwd()  # -> get current working directory
print(os.getcwd())

os.chdir(path + '/images')
print(os.getcwd())

os.chdir('..')
os.chdir(path + '/fonts')
print(os.getcwd())
