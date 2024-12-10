import requests
import json

def get_github_repos(query):
    """
    Отправляет GET-запрос к GitHub API для поиска репозиториев.

    Args:
        query: Строка поиска (например, "language:html").

    Returns:
        Словарь с данными ответа или None в случае ошибки.
    """
    url = f"https://api.github.com/search/repositories?q={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Поднимает исключение для не-2xx статусных кодов
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

if __name__ == "__main__":
    query = "language:html"  #  Поиск репозиториев с кодом HTML
    data = get_github_repos(query)

    if data:
        print(f"Статус-код: {data['total_count']}") #Выведем общее количество репозиториев
        print("Содержимое ответа (JSON):")
        print(json.dumps(data, indent=4)) #Форматированный вывод JSON
