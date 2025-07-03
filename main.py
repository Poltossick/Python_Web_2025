# Рекурсия
# def factorial(count): # 5! (факториал 5) = 1 * 2 * 3 * 4 * 5
#     result = 1
#     for i in range(2, count + 1):
#         result *= i
#     return result
#
# for x in range(6):
#     print(x, factorial(x))
from idlelib.tooltip import OnHoverTooltipBase


def factorial(count):
    if count <= 1:  # -> базовый вариант
        return 1  # -> базовый вариант
    return count * factorial(count - 1)  # -> рекурсивная / "пружина"


for x in range(6):
    print(x, factorial(x))
