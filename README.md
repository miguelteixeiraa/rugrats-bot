# RugratsBot


An Instagram bot that automates follow and comments.

```shell
# 1. install pip
sudo apt install python3-pip
# 2. install requestium
pip3 install requestium
# 3. Download https://chromedriver.storage.googleapis.com/index.html?path=85.0.4183.we38/
# 4. Put it extracted in the folder of this project
# 5. run
python3 bot_main.py
````

**Example:**
```python
# -*- coding: utf-8 -*-
from rugrats_bot import RugratsBot

# creating our baby rugrat and logging into your instagram account
rugratBot = RugratsBot("Your username", "Your password")
rugratBot.login()

# to follow all profiles that a profile follows
rugratBot.followProfiles("target user")

# get a user's number of followers
rugratBot.getNumberOfFollowers("target user")

# comment a publication by list of phrases/texts
rugratBot.commentingByList("instagram url to comment", "list of comments")

# comment a publication by web scrapping stuff
rugratBot.commentingByScrapingStuff("instagram url to comment", "subject to comment")
```

## Instagram limits:
**Accounts older than one year (recommended to not have got limited by instagram)**
 1. 10 - 15 comments per hour
 2. 600 - 1000 likes a day
 3. 60 - 80 new DMs
 4. 2200 characters in a post or comment (max recommended)
 5. 5 hashtags in a post or comment (max recommended) got


Make your own luck on instagram promotions :)



It will be completely written one day
