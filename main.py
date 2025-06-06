# main.py

from scrapers.nrl import fetch_nrl_news
from scrapers.zerotackle import fetch_zerotackle_news
import json

def main():
    print("Running main...")

    # 1) Scrape NRL
    nrl_news = fetch_nrl_news()

    # 2) Scrape Zero Tackle (RSS)
    zerotackle_news = fetch_zerotackle_news()

    # 3) Merge and sort
    all_news = nrl_news + zerotackle_news
    all_news.sort(key=lambda x: x['timestamp'], reverse=True)

    # 4) Print combined output
    print(f"Got {len(all_news)} total articles")
    print(json.dumps(all_news, indent=2))

    # 5) Save to JSON
    with open("latest_nrl_news.json", "w") as f:
        json.dump(all_news, f, indent=2)

if __name__ == "__main__":
    main()
