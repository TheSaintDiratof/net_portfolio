import requests

# URL для GET-запроса
get_url = 'https://jsonplaceholder.typicode.com/posts'

# Отправка GET-запроса
response_get = requests.get(get_url)

# Проверка кода ответа
if response_get.status_code == 200:
    print("GET-запрос успешен!")
    print("Содержимое страницы:")
    print(response_get.text[:500])  # Выводим первые 500 символов
else:
    print(f"Ошибка при GET-запросе: {response_get.status_code}")

# URL для POST-запроса
post_url = 'https://jsonplaceholder.typicode.com/posts'

# Данные для отправки
post_data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response_post = requests.post(post_url, json=post_data)

# Проверка кода ответа
if response_post.status_code == 201:
    print("POST-запрос успешен!")
    print("Полученные данные:")
    print(response_post.json())
else:
    print(f"Ошибка при POST-запросе: {response_post.status_code}")
