from requests import get, post, put, delete

# print(get('http://localhost:5000/api/news').json())
# print(get('http://localhost:5000/api/news/1').json())
# print(get('http://localhost:5000/api/news/1000').json())
# print(get('http://localhost:5000/api/news/q').json())

# print(post('http://localhost:5000/api/news', json={}).json())
# print(post('http://localhost:5000/api/news', json={'title': 'проверка заголовка'}).json())
# print(post('http://localhost:5000/api/news', json={'title': 'проверка заголовка',
#                                                    'content': 'содержание новости',
#                                                    'user_id': 3, 'is_private': False}).json())
# print(post('http://localhost:5000/api/news', json={'title': 'заголовок',
#                                                    'content': 'текст новости',
#                                                    'user_id': 2, 'is_private': False}).json())

print(delete('http://localhost:5000/api/news/500').json())