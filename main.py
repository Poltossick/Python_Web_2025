# ООП - объектно ориентированное программирование (encapsulation) - помещение объекта в капсулу
# инкапсуляция - сокрытие внутренней реализации с целью сокрытия внутренних данных

# АНАЛИЗ предыдущих вызовов
from lib import Car, Person, Clicker, Separator

nm = Separator()
for item in range(20):
    nm.add_num(item)
print(nm.get_odd())
print(nm.get_even())

