# ОС-модуль - работа с операционной системой

import os
path = os.getcwd()
os.chdir(path + '/images')

all_files = [f for f in os.listdir('.') if f.startswith('py')]
# обращаемся к конкретной директории ('.') - выше ее поменяли
print(all_files)
