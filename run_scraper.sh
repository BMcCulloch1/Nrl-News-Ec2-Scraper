#!/bin/bash

#Navigate to dir
cd /home/ec2-user/Rugby-News-

#Activate venv 
source venv/bin/activate

#Run main script with error logs 
python3 main.py >> logs/scraper.log 2>&1