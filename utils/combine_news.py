from scrapers.nrl import fetch_nrl_news
from scrapers.zerotackle import fetch_zerotackle_news

def get_combined_news():
    nrl_results = fetch_nrl_news()
    zerotackle_results = fetch_zerotackle_news()
    all_news = nrl_results + zerotackle_results
    all_news.sort(key = lambda x: x['timestamp'], reverse = True)
    return all_news
