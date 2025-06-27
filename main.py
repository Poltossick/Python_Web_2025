word = input('введите слово для зашифровки: ')
s = set()
res = ''
for ch in word:
    s.add(ord(ch))
print(s)
for item in s:
    res += chr(item)
print(res)
