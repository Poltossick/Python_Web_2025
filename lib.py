class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_left(self, weight:int) -> int:  # в граммах
       self.left += weight

    def add_right(self, weight:int) -> int:  # в граммах
        self.right += weight

    def result(self) -> str:
        if self.right < self.left:
            return 'Левая монетка перевесила'
        elif self.right > self.left:
            return 'Правая монетка перевесила'
        else:
            return 'Вес монеток одинаков'
