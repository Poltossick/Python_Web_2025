# return vs yield - возврат vs генератор

def generate_list():
    for item in range(5):
        return item  # возвращает значение и закрывает функцию


print(generate_list())  # 0
array = generate_list()
print(array)  # 0


def generate_list_2():
    for item in range(5):
        yield item  # генератор, возвращает и НЕ закрывает функцию


print(generate_list_2())  # <generator object generate_list_2 at 0x000001D01B45CDC0>
array_2 = list(generate_list_2())
print(array_2)  # [0, 1, 2, 3, 4]
