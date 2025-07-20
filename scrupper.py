import requests
from bs4 import BeautifulSoup

def fetch_hot_topics():
    url = "https://www.imo.org/en/MediaCentre/HotTopics/Pages/Default.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    topics = []
    for link in soup.find_all("a"):
        title = link.get_text(strip=True)
        href = link.get("href")
        if title and href and "/en/MediaCentre/HotTopics/Pages/" in href:
            full_link = "https://www.imo.org" + href
            topics.append({"title": title, "link": full_link})

    return topics

# Çıktıyı yazdır
topics = fetch_hot_topics()
for t in topics:
    print(f"{t['title']}\n{t['link']}\n")

input("Press Enter to exit...")