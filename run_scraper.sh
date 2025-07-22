#!/bin/bash

echo "Starting scraper at $(date)"

#Navigate to dir
cd /home/ec2-user/Rugby-News-

#Activate venv 
source venv/bin/activate

echo "Running scraper..."

#Run main script with error logs 
python3 main.py >> logs/manual_run.log 2>&1

echo "Python script finished running"

echo "Finished scraper run at $(date)"
