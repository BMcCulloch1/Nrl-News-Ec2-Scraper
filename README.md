# NRL News Scraper

A small Python project that scrapes National Rugby League (NRL) and Zero Tackle news, saves the articles as JSON, and uploads the results to an AWS S3 bucket. It’s designed to run automatically on an EC2 instance.

---

## What It Does

- Scrapes articles from NRL and Zero Tackle using Playwright + BeautifulSoup  
- Merges and sorts results by timestamp  
- Removes duplicate articles (based on URL)  
- Saves two files:  
  - `latest_nrl_news.json`: 5 newest articles per source  
  - `all_nrl_news.json`: full history of articles (deduplicated)  
- Uploads both files to an S3 bucket using `boto3`

---

## Setup Instructions

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

Configure AWS credentials using the AWS CLI:

```bash
aws configure
```

Or set them as environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=your_region
```

Set up your S3 bucket:

Update the bucket name in `utils/upload.py` or in a `.env` file if you're using one.

Test the scraper:

```bash
python main.py
```

This should generate:

- `latest_nrl_news.json`  
- `all_nrl_news.json`  

These will be saved in the `data/` directory and uploaded to your configured S3 bucket.

---

## Cron Setup

This project uses a cron job on your EC2 instance:

- Hourly: Runs the scraper every hour  

Install the cron jobs:

```bash
crontab crontab.txt
```

Example `crontab.txt` content:

```cron
0 * * * * /home/ec2-user/YOUR_REPO/run_scraper.sh >> /home/ec2-user/YOUR_REPO/logs/cron.log 2>&1
```

Make sure the shell script is executable:

```bash
chmod +x run_scraper.sh
```

---

## File Structure

```
nrl-news-scraper/
├── crontab.txt
├── data/
├── logs/
├── scrapers/
│   ├── nrl.py
│   └── zerotackle.py
├── utils/
│   ├── upload.py
│   └── combine_news.py
├── run_scraper.sh
├── main.py
├── requirements.txt
```

---

## Notes

- Designed to be low-cost and efficient by using EC2 + S3 (no Lambda for scraping).
- S3 filenames are overwritten with fresh data to keep it lightweight for API consumption.
- Pairs with the `nrl-news-frontend` React app via a public AWS Lambda API.
