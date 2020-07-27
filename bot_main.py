# -*- coding: utf-8 -*-
from rugrats_bot import RugratsBot


# creating our baby rugrat
rugratBot = RugratsBot()
rugratBot.setLoginInfo("Your instagram username", "Your instagram password")

listOfComments = [
    # your string list of possible comments here
]
rugratBot.setListOfComments(listOfComments)

# url of the publication to send comments
rugratBot.setInstagramPageUrl("https://www.instagram.com/TargetUrl")

# now, just watch our baby rugrat having fun with your instagram account
rugratBot.startCommenting()
