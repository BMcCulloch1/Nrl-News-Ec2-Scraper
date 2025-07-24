# main.py

from scrapers.nrl import fetch_nrl_news
from scrapers.zerotackle import fetch_zerotackle_news
from utils.upload import upload_json_to_s3
from utils.combine_news import get_combined_news  
import json
import boto3
import os

# Global Variables 
DATA_DIR = "data"
MASTER_FILE = os.path.join(DATA_DIR, "all_nrl_news.json")
LATEST_FILE = os.path.join(DATA_DIR, "latest_nrl_news.json")

### Helper Functions ###

# Load Articles 
def load_articles(filepath):
    if not os.path.exists(filepath):
        return[]
    with open(filepath, "r") as f:
        return json.load(f)

# Load Articles
def save_articles(filepath, articles):
    with open(filepath, "w") as f:
        json.dump(articles, f, indent = 2)

# Delete Duplicates
def delete_duplicates(articles):
    seen = set()
    unique = []
    for article in articles:
        if article["url"] not in seen:
            seen.add(article["url"])
            unique.append(article)
    return unique

# Get the 5 lastest articles from each News Source
def get_5_latest_articles(articles, limit = 5):
    grouped = {}
    for article in articles:
        grouped.setdefault(article["source"], []).append(article)
    latest = []
    for source, group in grouped.items():
        group.sort(key = lambda x: x["timestamp"], reverse = True)
        latest.extend(group[:limit])
    return latest

    

def main():
    print("Running main...")

    # Scrape NRL news sites
    fresh_articles = get_combined_news()

    # Load Master news file 
    all_articles = load_articles(MASTER_FILE)

    # Add new articles and delete dups
    all_articles += fresh_articles
    all_articles = delete_duplicates(all_articles)

    # Save Master file 
    save_articles(MASTER_FILE, all_articles)
    print(f"Saved Master File with {len(all_articles)} unique articles")

    # Get 5 latest articles per sources 
    latest_articles = get_5_latest_articles(all_articles)
    save_articles(LATEST_FILE, latest_articles)
    print(f"Saved latest news file with {len(latest_articles)} articles")

    # Upload to s3 bucket
    bucket_name = "nrl-bucket-latest-news"
    key_name = "latest_nrl_news.json"

    # Upload latest file
    upload_json_to_s3(latest_articles, bucket_name, "latest_nrl_news.json")
    print(f"Uploaded latest to S3: {bucket_name}/latest_nrl_news.json")

    # Upload master file
    upload_json_to_s3(all_articles, bucket_name, "all_nrl_news.json")
    print(f"Uploaded master to S3: {bucket_name}/all_nrl_news.json")

        

if __name__ == "__main__":
    main()
