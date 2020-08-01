# -*- coding: utf-8 -*-
from rugrats_bot import RugratsBot


# creating our baby rugrat and logging into your instagram account
rugratBot = RugratsBot("your username", "your password")
rugratBot.login()

# follow users of a target user
rugratBot.followProfilesTargetProfile("target user")
