# main.py

from scrapers.nrl import fetch_nrl_news
from scrapers.zerotackle import fetch_zerotackle_news
from utils.upload import upload_json_to_s3
import json
import boto3

def main():
    print("Running main...")

    # Scrape NRL
    nrl_news = fetch_nrl_news()

    # Scrape Zero Tackle (RSS)
    zerotackle_news = fetch_zerotackle_news()

    # Merge and sort
    all_news = nrl_news + zerotackle_news
    all_news.sort(key=lambda x: x['timestamp'], reverse=True)

    # Print combined output
    print(f"Got {len(all_news)} total articles")
    print(json.dumps(all_news, indent=2))

    # Save to JSON
    with open("latest_nrl_news.json", "w") as f:
        json.dump(all_news, f, indent=2)


    # Upload to s3 bucket
    bucket_name = "nrl-bucket-latest-news"
    key_name = "latest_nrl_news.json"
    upload_json_to_s3(all_news, bucket_name, key_name)
    print(f"Uploaded to S3: {bucket_name}/{key_name}")
        





if __name__ == "__main__":
    main()
