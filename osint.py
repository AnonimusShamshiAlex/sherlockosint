import requests

def search_platform(username, platform_name, url_template):
    print(f"\n🔍 Поиск в {platform_name}: {username}")
    url = url_template.format(username=username)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✅ Профиль найден: {url}")
        else:
            print(f"❌ Профиль не найден в {platform_name}.")
    except Exception as e:
        print(f"⚠️ Ошибка при поиске в {platform_name}: {e}")

if __name__ == "__main__":
    print("=== OSINT Tool ===")
    username = input("Введите ник или имя для поиска: ").strip()

    # Список платформ и шаблонов URL
    platforms = [
        ("Facebook", "https://www.facebook.com/{username}"),
        ("YouTube", "https://www.youtube.com/results?search_query={username}"),
        ("Instagram", "https://www.instagram.com/{username}/"),
        ("WhatsApp", "https://wa.me/{username}"),
        ("WeChat", "https://www.wechat.com/{username}"),
        ("Messenger", "https://www.messenger.com/t/{username}"),
        ("Telegram", "https://t.me/{username}"),
        ("Snapchat", "https://www.snapchat.com/add/{username}"),
        ("Pinterest", "https://www.pinterest.com/{username}/"),
        ("Twitter (X)", "https://x.com/{username}"),
        ("LinkedIn", "https://www.linkedin.com/in/{username}"),
        ("Reddit", "https://www.reddit.com/user/{username}"),
        ("Quora", "https://www.quora.com/profile/{username}"),
        ("Discord", "https://discord.com/users/{username}"),
        ("Viber", "https://www.viber.com/{username}"),
        ("Line", "https://line.me/{username}"),
        ("KakaoTalk", "https://www.kakaocorp.com/service/KakaoTalk/{username}"),
        ("Weibo", "https://weibo.com/{username}"),
        ("Tumblr", "https://{username}.tumblr.com"),
        ("Clubhouse", "https://www.clubhouse.com/@{username}"),
        ("Twitch", "https://www.twitch.tv/{username}"),
        ("Vimeo", "https://vimeo.com/{username}"),
        ("Dailymotion", "https://www.dailymotion.com/{username}"),
        ("Bilibili", "https://space.bilibili.com/{username}"),
        ("Likee", "https://likee.video/@{username}"),
        ("Tinder", "https://tinder.com/@{username}"),
        ("Bumble", "https://bumble.com/{username}"),
        ("Hinge", "https://hinge.co/{username}"),
        ("OkCupid", "https://www.okcupid.com/profile/{username}"),
        ("Grindr", "https://www.grindr.com/{username}"),
        ("Spotify", "https://open.spotify.com/user/{username}"),
        ("SoundCloud", "https://soundcloud.com/{username}"),
        ("Bandcamp", "https://{username}.bandcamp.com"),
        ("Behance", "https://www.behance.net/{username}"),
        ("Dribbble", "https://dribbble.com/{username}"),
        ("GitHub", "https://github.com/{username}"),
        ("VK (ВКонтакте)", "https://vk.com/{username}"),
        ("Odnoklassniki", "https://ok.ru/{username}"),
        ("Xing", "https://www.xing.com/profile/{username}"),
        ("Zalo", "https://zalo.me/{username}"),
        ("Flickr", "https://www.flickr.com/people/{username}/"),
        ("Meetup", "https://www.meetup.com/members/{username}/"),
        ("Nextdoor", "https://nextdoor.com/profile/{username}"),
        ("Goodreads", "https://www.goodreads.com/{username}"),
        ("Strava", "https://www.strava.com/athletes/{username}")
    ]

    # Поиск на всех платформах
    for platform_name, url_template in platforms:
        search_platform(username, platform_name, url_template)
