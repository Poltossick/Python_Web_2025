# ООП - объектно ориентированное программирование (encapsulation) - помещение объекта в капсулу
# инкапсуляция - сокрытие внутренней реализации с целью сокрытия внутренних данных

# АНАЛИЗ предыдущих вызовов
from lib import Car, Person, Clicker

a = Clicker()
a.click()
a.click()
a.click()
a.click()
a.click()
print(a.click_counter())

a.reset()
print(a.click_counter())