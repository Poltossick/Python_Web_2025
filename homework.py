stop_words = ['ну', 'типо', 'короче']
text = ''
lst = ''
while (message := input('Введите сообщение: ')) != '': #ну я типо вообще короче не понимаю это язык
    lst = message.split()
for item in lst:
    if item in stop_words:
        item = ''
    else:
        text += item + ' '
res = ' '.join(text.split())
print(res)
res = sorted(res.split())
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')