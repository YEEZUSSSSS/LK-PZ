from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def get_wikipedia_paragraphs(driver, url):
    """Извлекает параграфы с Википедии."""
    driver.get(url)
    time.sleep(2) # Время для загрузки страницы
    paragraphs = []
    try:
        for p in driver.find_elements(By.TAG_NAME, "p"):
            paragraphs.append(p.text)
    except NoSuchElementException:
        print("Параграфы не найдены на странице.")
    return paragraphs

def get_wikipedia_links(driver):
    """Получает ссылки на связанные страницы."""
    links = []
    try:
        for a in driver.find_elements(By.CSS_SELECTOR, "a.mw-link"): #Селектор нужно может быть изменен, зависит от структуры Википедии
            href = a.get_attribute("href")
            if href and "wikipedia" in href: #Проверка, что это ссылка внутри Википедии
              links.append((a.text, href))
    except NoSuchElementException:
      print("Ссылки не найдены на странице.")
    return links


if __name__ == "__main__":
    driver = webdriver.Chrome() # Замените на ваш webdriver

    initial_query = input("Введите ваш поисковой запрос на Википедии (на английском): ")
    search_url = f"https://en.wikipedia.org/wiki/{initial_query.replace(' ', '_')}"


    while True:
        paragraphs = get_wikipedia_paragraphs(driver, search_url)
        if paragraphs:
            for i, paragraph in enumerate(paragraphs):
                print(f"\nПараграф {i+1}:\n{paragraph}")


        links = get_wikipedia_links(driver)
        if links:
            print("\nСвязанные страницы:")
            for i, (title, link) in enumerate(links[:3]): #Отображаем только первые 3 ссылки
                print(f"{i+1}. {title} ({link})")


        print("\nВыберите действие:")
        print("1. Листать параграфы")
        print("2. Перейти на связанную страницу")
        print("3. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            continue # Остаемся на текущей странице

        elif choice == "2":
            if links:
                try:
                  link_choice = int(input("Введите номер страницы: ")) - 1
                  if 0 <= link_choice < len(links):
                    search_url = links[link_choice][1]
                  else:
                    print("Неверный номер страницы.")
                except ValueError:
                  print("Неверный ввод.")
            else:
              print("Нет связанных страниц.")

        elif choice == "3":
            break

        else:
            print("Неверный выбор.")

    driver.quit()
