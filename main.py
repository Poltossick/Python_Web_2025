# потоковый ввод - sys.stdin - итератор (подобно range), двигается только вперед,
# чтобы завершить, нужно нажать ctrl + D
# (!) input() - строковый ввод
import sys

# data = sys.stdin.readlines()
# print(data) # -> ['Привет\n', 'Как дела?\n', 'Что делаешь?\n']
text = [d.strip('\n') for d in sys.stdin.readlines()]
# print(' - '.join(sorted(text, key=lambda s: s[1]))) # -> Привет! Как дела? Пока
t = list(enumerate(text))
t.sort(key=lambda y: y[1])
index = t[0][0]
res = sorted(text[index].split())
print(*res, sep='-')

temp = []  # индекс строки в text и число слов в виде картежа
for indx, srtl in enumerate(text):
    temp.append((indx, len(srtl.split())))
temp.sort(key=lambda y: y[1])
index = temp[0][0]
res = sorted(text[index].split())
print(*res, sep='-')


# неверное  for line in text:
#     if len(line) == 2:
#         print(' - '.join(sorted(line, key=lambda s: s[0])))
#     else:
#         pass
