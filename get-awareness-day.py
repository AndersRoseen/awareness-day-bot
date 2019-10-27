#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime

todays_date = datetime.today().date().strftime("%d %b %Y")
# todays_date = '27 Oct 2019'

# Get awareness days
with open('awareness-days.json', 'r', encoding="utf-8") as f:
  days_dict = json.load(f)
  for day in days_dict:
    day_date = day["Date"]       # datetime.strptime(day["Date"], '%d %b %Y').date()
    if day_date == todays_date:
      theme_list = day["Theme"]
      # break

print(todays_date)
for theme in theme_list:
  print(' * ' + theme)

# Post theme_list and todays_date to Slack
print("Posting to Slack...")
