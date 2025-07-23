# mail_test.py
# pip install python-dotenv
import smtplib

from mail_sender import send_mail

send_mail('1812.lev@gmail.com', 'Вам письмо', 'Текст письма для проверки')

# try:
#     server = smtplib.SMTP('smtp.yandex.ru', 465)
#     server.starttls()
#     server.login('polly.petrovna@yandex.ru', 'higmoodhegxqdmnz')
#     print("Доступ к SMTP сервису успешно установлен")
#     server.quit()
# except Exception as e:
#     print(f"Ошибка при подключении: {e}")

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# try:
#     # Настройки SMTP для Яндекса
#     smtp_server = 'smtp.yandex.ru'
#     port = 587
#     email = 'polly.petrovna@yandex.ru'
#     password = 'higmoodhegxqdmnz'  # Или пароль приложения, если включена 2FA
#
#     # Создание сообщения
#     msg = MIMEMultipart()
#     msg['From'] = email
#     msg['To'] = '1812.lev@gmail.com'
#     msg['Subject'] = 'Тестирование SMTP Яндекс'
#
#     # Текст письма
#     body = 'Это тестовое письмо, отправленное через Python и Яндекс SMTP'
#     msg.attach(MIMEText(body, 'plain'))
#
#     # Подключение к серверу
#     server = smtplib.SMTP(smtp_server, port)
#     server.ehlo()
#     server.starttls()
#     server.login(email, password)
#
#     # Отправка письма
#     server.sendmail(email, msg['To'], msg.as_string())
#     print("Письмо успешно отправлено!")
#
#     # Закрытие соединения
#     server.quit()
#
# except smtplib.SMTPAuthenticationError:
#     print("Ошибка аутентификации. Проверьте логин и пароль.")
# except smtplib.SMTPServerDisconnected:
#     print("Сервер SMTP отключился. Проверьте настройки подключения.")
# except Exception as e:
#     print(f"Произошла ошибка: {e}")