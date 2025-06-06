from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime
import re


def fetch_nrl_news():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.nrl.com/news/")
        page.wait_for_timeout(3000)

        soup = BeautifulSoup(page.content(), 'html.parser')
        articles = soup.select('a.card')[:5]

        news_list = []
        for article in articles:
            raw_title = article.get_text(strip=True)
            title = clean_title(raw_title)
            href = article.get('href')
            if title and href:
                news_list.append({
                    "source": "NRL",
                    "title": title,
                    "url": "https://www.nrl.com" + href,
                    "timestamp": datetime.utcnow().isoformat()
                })

        browser.close()
        return news_list
    

def clean_title(title):
    return re.sub(r'^\d{1,2}:\d{2}', '', title).strip()

if __name__ == "__main__":
    news = fetch_nrl_news()
    for article in news:
        print(article)
