import requests
import json

def create_post(data):
    """
    Отправляет POST-запрос к API jsonplaceholder для создания новой записи.

    Args:
        data: Словарь с данными для новой записи.

    Returns:
        Словарь с данными ответа или None в случае ошибки.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {'Content-type': 'application/json'} #Важно указать тип данных в заголовке

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP-статуса
        new_post = response.json()
        return new_post
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке POST-запроса: {e}")
        return None

if __name__ == "__main__":
    new_post_data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response_data = create_post(new_post_data)

    if response_data:
        print(f"Статус-код: {response_data.get('statusCode', response_data.get('status'))}") #Обработка разных форматов ответа
        print("Содержимое ответа:")
        print(json.dumps(response_data, indent=2))
