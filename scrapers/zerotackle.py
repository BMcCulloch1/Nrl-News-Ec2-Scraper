# scrapers/zerotackle.py

import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def fetch_zerotackle_news():
    """
    Fetches the latest five articles from Zero Tackle’s RSS feed
    using requests + xml.etree.ElementTree.
    """
    feed_url = "https://www.zerotackle.com/feed/"
    try:
        response = requests.get(feed_url, timeout=15)
        response.raise_for_status()
    except Exception as e:
        # Could not fetch the feed
        print(f"[ERROR] Failed to fetch RSS feed: {e}")
        return []

    # Parse the XML content
    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as e:
        print(f"[ERROR] Failed to parse XML: {e}")
        return []

    # In RSS 2.0, items live under channel/item
    channel = root.find("channel")
    if channel is None:
        print("[ERROR] <channel> tag not found in RSS feed")
        return []

    items = channel.findall("item")[:5]
    news_list = []

    for item in items:
        title_tag = item.find("title")
        link_tag  = item.find("link")

        if title_tag is None or link_tag is None:
            continue

        title = (title_tag.text or "").strip()
        url   = (link_tag.text or "").strip()

        if not title or not url:
            continue

        news_list.append({
            "source": "ZeroTackle",
            "title": title,
            "url": url,
            "timestamp": datetime.utcnow().isoformat()
        })

    return news_list

# Standalone test block
if __name__ == "__main__":
    news = fetch_zerotackle_news()
    print(f"[DEBUG] Returning {len(news)} articles\n")
    for article in news:
        print(article)
