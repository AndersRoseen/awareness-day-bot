#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime
import sys
import urllib.request
import urllib.error

todays_date = datetime.today().date().strftime("%d %b %Y")
# todays_date = '24 Nov 2019'

# Get awareness days
with open('awareness-days.json', 'r', encoding="utf-8") as f:
  days_dict = json.load(f)
  for day in days_dict:
    day_date = day["Date"]       # datetime.strptime(day["Date"], '%d %b %Y').date()
    if day_date == todays_date:
      theme_list = day["Theme"]
      # break

try:
  theme_list
except NameError:
  print("No special day to celebrate today...")
  sys.exit()

theme_list_text = ''
for theme in theme_list:
  theme_list_text += '- ' + theme + '\n'

# Post theme days to Slack channel #random
webhook_url = 'https://hooks.slack.com/services/###' # Post to #test
#webhook_url = 'https://hooks.slack.com/services/###' # Post to #random
slack_data = { "blocks": [
        {
          "type": "section",
          "text": {
            "type": "mrkdwn",
            "text": theme_list_text
          }
        }
    ]}
headers = {'Content-type': 'application/json'}

data_bytes = json.dumps(slack_data).encode("utf-8")
req = urllib.request.Request(webhook_url, data_bytes, headers)

try:
    post_response = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except urllib.error.URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
