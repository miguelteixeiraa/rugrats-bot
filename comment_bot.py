# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver

class CommentBot:
    def __init__(self):
        self._instagramPageUrl = str()
        self._userLogin = str()
        self._userPassword = str()
        self._listOfComments = list()
        self._rangeTimeBetComments = range(10) #default range seconds between comments
        self._browserBot = webdriver.Firefox()

    def setLoginInfo(self, userLogin, userPass):
        self._userLogin = userLogin
        self._userPassword = userPass

    def setInstagramPageUrl(self, instaPageUrl):
        self._instagramPageUrl = instaPageUrl

    def setListOfComments(self, listOfComments):
        self._listOfComments = listOfComments

    def setTimeBetComments(self, timeBetweenComments):
        self._rangeTimeBetComments = timeBetweenComments

    def startWork(self):
        self._browserBot.implicitly_wait(10)
        self._browserBot.get('https://www.instagram.com/')
