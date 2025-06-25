hour = 13
if hour > 23:
    hour = 23
if hour < 0:
    hour = 0

if 7 <= hour < 12:
    print('Доброе утро')
elif 12 <= hour < 18:
    print('Добрый день')
elif 18 <= hour < 23:
    print('Добрый вечер')
else:
    print('Доброй ночи')
