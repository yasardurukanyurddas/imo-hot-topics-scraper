from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

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
        if title and href and "/en/MediaCentre/HotTopics/Pages/" in href:
            full_link = "https://www.imo.org" + href
            topics.append({"title": title, "link": full_link})

    return topics

@app.route("/")
def home():
    topics = fetch_hot_topics()
    return render_template_string("""
    <html>
    <head>
    background: url('{{ url_for('static', filename='arka.jpg') }}') no-repeat center center fixed;
        <title>IMO Hot Topics</title>
        <style>
            body { font-family: Arial; background: #f5f5f5; padding: 40px; }
            h1 { color: #004080; }
            ul { list-style: none; padding: 0; }
            li { margin-bottom: 12px; }
            a { text-decoration: none; color: #0077cc; font-size: 18px; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>📌 IMO Hot Topics</h1>
        <ul>
            {% for topic in topics %}
                <li><a href="{{ topic.link }}" target="_blank">{{ topic.title }}</a></li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """, topics=topics)

if __name__ == "__main__":
    app.run(debug=True)