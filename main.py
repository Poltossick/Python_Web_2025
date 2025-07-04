# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)
import pprint  # -> "pretty-printer"

matrix = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
matrix.insert(0, matrix)
# print(matrix)
pprint.pprint(matrix)

