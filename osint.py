import requests
from bs4 import BeautifulSoup

def search_google(query):
    print(f"\n🔍 Поиск в Google: {query}")
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('h3')
        if results:
            print("Результаты Google:")
            for result in results[:5]:  # Показываем первые 5 результатов
                print(f"- {result.text}")
        else:
            print("Нет результатов в Google.")
    else:
        print("Ошибка при поиске в Google.")

def search_instagram(username):
    print(f"\n🔍 Поиск в Instagram: {username}")
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Профиль найден: {url}")
    else:
        print("❌ Профиль не найден в Instagram.")

def search_tiktok(username):
    print(f"\n🔍 Поиск в TikTok: {username}")
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Профиль найден: {url}")
    else:
        print("❌ Профиль не найден в TikTok.")

def search_youtube(query):
    print(f"\n🔍 Поиск в YouTube: {query}")
    url = f"https://www.youtube.com/results?search_query={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', {'id': 'video-title'})
        if results:
            print("Результаты YouTube:")
            for result in results[:5]:  # Показываем первые 5 результатов
                print(f"- {result.text.strip()}")
        else:
            print("Нет результатов в YouTube.")
    else:
        print("Ошибка при поиске в YouTube.")

if __name__ == "__main__":
    print("=== OSINT Tool ===")
    query = input("Введите ник или имя для поиска: ").strip()
    search_google(query)
    search_instagram(query)
    search_tiktok(query)
    search_youtube(query)
