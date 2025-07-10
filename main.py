# ООП - (polymorphism)

from lib import Stat

lst = list(range(1, 15))

st = Stat(lst)
print(st.get_min())
print(st.get_max())
print(st.get_average())
