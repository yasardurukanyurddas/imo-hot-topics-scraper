import requests
from bs4 import BeautifulSoup

def fetch_hot_topics():
    url = "https://www.imo.org/en/MediaCentre/HotTopics/Pages/Default.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    topics = []
    for link in soup.find_all("a"):
        title = link.get_text(strip=True)
        href = link.get("href")
        # URL yerine sadece başlığı al
        if title and href and "/en/MediaCentre/HotTopics/Pages/" in href:
            topics.append(title)

    return topics

# Çıktıyı yazdır
topics = fetch_hot_topics()
print("📌 IMO Hot Topics Başlıkları:\n")
for i, t in enumerate(topics, start=1):
    print(f"{i}. {t}")

input("\nKapatmak için Enter'a bas...")