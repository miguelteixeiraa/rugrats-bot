# RugratsBot


An Instagram bot that automates follow and comments (tagging people too).

1. install pip -> sudo apt install python3-pip
2. install requestium -> pip3 install requestium
3. run -> python3 bot_main.py
4. have fun!

**Example:**

```python
from rugrats_bot import RugratsBot


# creating our baby rugrat
rugratBot = RugratsBot()
rugratBot.setLoginInfo("Your instagram username", "Your instagram password")

listOfComments = [
    # your string list of possible comments here
]
rugratBot.setListOfComments(listOfComments)

# url of publication to send comments
rugratBot.setInstagramPageUrl("https://www.instagram.com/TargetUrl")

# now, just watch our baby rugrat having fun with your instagram account
rugratBot.startCommenting()
```


Make your own luck on instagram promotions :)



It will be completely written one day
