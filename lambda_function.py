import json
import boto3
from scrapers.nrl import fetch_nrl_news
from scrapers.zerotackle import fetch_zerotackle_news
from utils.combine_news import get_combined_news
from utils.upload import upload_json_to_s3




## Lamda function runs inside AWS lamda. It extracts all scraped
#  data from NRL and converts into JSON and uploads to S3.

def lambda_handler(event, context):
    all_news = get_combined_news()
    bucket_name = 'nrl-bucket-latest-news'
    key_name = 'latest-news.json'
    upload_json_to_s3(all_news, bucket_name, key_name)


  
if __name__ == "__main__":
    lambda_handler({}, {})  