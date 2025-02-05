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

def search_facebook(username):
    print(f"\n🔍 Поиск в Facebook: {username}")
    url = f"https://www.facebook.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Профиль найден: {url}")
    else:
        print("❌ Профиль не найден в Facebook.")

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

def search_snapchat(username):
    print(f"\n🔍 Поиск в Snapchat: {username}")
    url = f"https://www.snapchat.com/add/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Профиль найден: {url}")
    else:
        print("❌ Профиль не найден в Snapchat.")

def search_reddit(username):
    print(f"\n🔍 Поиск в Reddit: {username}")
    url = f"https://www.reddit.com/user/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Профиль найден: {url}")
    else:
        print("❌ Профиль не найден в Reddit.")

def search_linkedin(username):
    print(f"\n🔍 Поиск в LinkedIn: {username}")
    url = f"https://www.linkedin.com/in/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Профиль найден: {url}")
    else:
        print("❌ Профиль не найден в LinkedIn.")

def search_pinterest(username):
    print(f"\n🔍 Поиск в Pinterest: {username}")
    url = f"https://www.pinterest.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Профиль найден: {url}")
    else:
        print("❌ Профиль не найден в Pinterest.")

if __name__ == "__main__":
    print("=== OSINT Tool ===")
    query = input("Введите ник или имя для поиска: ").strip()
    search_google(query)
    search_instagram(query)
    search_facebook(query)
    search_youtube(query)
    search_snapchat(query)
    search_reddit(query)
    search_linkedin(query)
    search_pinterest(query)
