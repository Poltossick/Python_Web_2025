stop_words = ['ну', 'типо', 'короче']
text = []
message = input('Введите сообщение: ') #  ну я типо вообще короче не понимаю это язык
lst = message.split() # все слова
for item in lst:
    if item not in stop_words:
        text.append(item)
res = sorted(text)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')


stop_words = {'ну', 'типо', 'короче'}
text = set()
message = input('Введите сообщение: ') #  ну я типо вообще короче не понимаю это язык
lst = message.split() # все слова
for item in lst:
    if item not in stop_words:
        text.add(item)
res = sorted(text)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')

stop_words = {'ну', 'типо', 'короче', 'не'}
message = input('Введите сообщение: ')  # ну я типо вообще короче не понимаю это язык
lst = message.split()  # все слова
text = set(lst) - stop_words
res = sorted(text)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')