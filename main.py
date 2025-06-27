word = '     привет      '
print(word.strip())
print(word.lstrip())
print(word.rstrip())

word = 'ротор'
print(word.strip('р'))
print(word.lstrip('р'))
print(word.rstrip('р'))

temp = input('Введите слово: ').strip()
print(temp)
