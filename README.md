# NRL News Scraper

A small Python project that scrapes National Rugby League (NRL) and Zero Tackle news, saves the articles as JSON, and uploads the results to an AWS S3 bucket. It’s designed to run automatically on an EC2 instance.

## What It Does

- Scrapes articles from NRL and Zero Tackle using Playwright + BeautifulSoup  
- Merges and sorts results by timestamp  
- Removes duplicate articles (based on URL)  
- Saves two files:
  - `latest_nrl_news.json`: 5 newest articles per source  
  - `all_nrl_news.json`: full history of articles (deduplicated)  
- Uploads both files to an S3 bucket using `boto3`

## Cron Setup

This project uses two cron jobs on EC2:

- **Hourly**: Runs the scraper every hour  

To set up the cron jobs:

```bash
crontab crontab.txt
