# value = "значение"
# text = f"Вот пример: {value:>10}"  # Добавляет 10 пробелов справа от значения
# print(text)

login = input('Введите логин: ')
birthday = input('Введите дату рождения в формате ДД-ММ-ГГГГ: ')
email = input('Введите адрес электронной почты: ')
password = input('Введите пароль из 6 знаков: ')
if (len(birthday) == 10 and len(password) == 6):
    print('Проверка данных:')
    print(f'\tЛогин: {login:>16}', f'\n\tДата рождения: {birthday:>14}', f'\n\tЭлектронная почта: {email}',
          f'\n\tПароль: {password:>17}')
else:
    print('Проверьте корректность заполненных данных')
