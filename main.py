# ООП - (inheritance) наследование
from lib import BankAccount

cl1 = BankAccount('Petr')
cl1.deposit(15)
cl1.withdraw(0)
cl1.withdraw(10)
cl1.get_balance()