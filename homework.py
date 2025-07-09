from lib import Balance


b = Balance()

b.add_left(5)
b.add_right(4)
b.add_right(2)
b.add_left(5)
b.add_right(4)



print(b.result())
