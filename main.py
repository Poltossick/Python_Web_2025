# Сериализация

import pickle
import pprint

# dic = {
#     'table': 'стол',
#     'chair': 'стул'
# }
#
# with open('./documents/dictfile.dat', 'wb') as pcl:
#     # dic - что сериализуем
#     # pcl - куда сериализуем
#     pickle.dump(dic, pcl)

# Десериализация

# with open('./documents/dictfile.dat', 'rb') as pcl:
#     # dic - что будет загружено
#     # pcl - откуда будет загружено
#     dic = pickle.load(pcl)
#
# pprint.pprint(dic, width=20)

from path_lib import *
print(img_dir)
print(font_dir)
print(doc_dir)
print(test)