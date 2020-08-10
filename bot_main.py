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
