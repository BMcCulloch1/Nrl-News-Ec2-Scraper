### NRL-News
A personal project that scrapes National Rugby League (sport) and Zero Tackle news, stores it in S3, and runs automatically on an AWS EC2 instance.


### Cron Setup

This project uses two cron jobs:

- Every hour: Runs the scraper and uploads news to S3.
- On reboot: Ensures the scraper runs if the EC2 restarts.

See `crontab.txt` for config/setup.

To install on EC2 inst.:
```bash
crontab crontab.txt