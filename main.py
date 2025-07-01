commas = (',', '.', '!', '?', '-')

stop_words = {'ну', 'типо', 'короче', 'не'}
message = input('Введите сообщение: ')  # ну я, типо! вообще - короче? не понимаю. это язык
for z in commas:
    message = message.replace(z, '')
lst = message.split()  # все слова
text = set(lst) - stop_words
res = sorted(text)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')