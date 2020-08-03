# -*- coding: utf-8 -*-
from rugrats_bot import RugratsBot

# creating our baby rugrat and logging into your instagram account
rugratBot = RugratsBot("Your username", "Your password")
rugratBot.login()

# follow all profiles a user follows
rugratBot.followProfilesTargetProfile("Target user")
