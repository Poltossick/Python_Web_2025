# ООП - (polymorphism)

from lib import Selector

lst = list(range(1, 15))

sel = Selector(lst)
print(sel.get_odd())
print(sel.get_even())
print(lst)

