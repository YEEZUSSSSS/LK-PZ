import requests
import json

def get_posts_by_user(user_id):
    """
    Отправляет GET-запрос к API jsonplaceholder с параметром userId.

    Args:
        user_id: ID пользователя.

    Returns:
        Список словарей с записями или None в случае ошибки.
    """
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки в HTTP-статусе
        posts = response.json()
        return posts
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

if __name__ == "__main__":
    user_id = 1
    posts = get_posts_by_user(user_id)

    if posts:
        print(f"Записи пользователя с ID {user_id}:")
        for post in posts:
            print(json.dumps(post, indent=2)) #Вывод каждой записи в красивом формате JSON
