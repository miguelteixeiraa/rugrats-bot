# -*- coding: utf-8 -*-
import sys
import os
from random import randrange
from time import sleep

from requestium import Session
from requests import ConnectionError


class RugratsBot:
    def __init__(self):
        self._rugratSession = Session(
            "./chromedriver", browser="chrome", default_timeout=15
        )
        self._instagramPageUrl = str()
        self._userLogin = str()
        self._userPassword = str()
        self._listOfComments = list()

        # default range seconds between comments
        self._rangeTimeBetComments = 59

    def setLoginInfo(self, userLogin, userPass):
        self._userLogin = userLogin
        self._userPassword = userPass

    def setInstagramPageUrl(self, instaPageUrl):
        self._instagramPageUrl = instaPageUrl

    def setListOfComments(self, listOfComments):
        self._listOfComments = listOfComments

    def setTimeBetComments(self, timeBetweenComments):
        self._rangeTimeBetComments = timeBetweenComments

    def isInternetOn(self):
        url = "http://www.google.com/"
        timeout = 5
        try:
            _ = self._rugratSession.get(url, timeout=timeout)
            return True
        except ConnectionError:
            print("No connection available")
        return False

    def startCommenting(self):

        # Sign in on instagram **outset**
        self._rugratSession.driver.get(
            "https://www.instagram.com/accounts/login/?hl=pt-br"
        )
        sleep(5)

        self._rugratSession.driver.ensure_element_by_css_selector(
            "input[name='username']"
        ).send_keys(self._userLogin)
        self._rugratSession.driver.ensure_element_by_css_selector(
            "input[name='password']"
        ).send_keys(self._userPassword)

        sleep(5)
        self._rugratSession.driver.ensure_element_by_xpath(
            "/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]"
        ).click()
        # Sign in on instagram **end**

        # Save login information on Chromium driver **outset**
        sleep(5)
        self._rugratSession.driver.ensure_element_by_xpath(
            "/html/body/div[1]/section/main/div/div/div/section/div/button"
        ).click()

        sleep(5)
        self._rugratSession.driver.ensure_element_by_xpath(
            "/html/body/div[4]/div/div/div/div[3]/button[1]"
        ).click()
        # Save login information on Chromium driver **end**

        # Load target instagram page **outset**
        self._rugratSession.driver.get(self._instagramPageUrl)
        # Load target instagram page **end**

        # start commenting
        while True:
            try:
                index = randrange(0, len(self._listOfComments))
                sleepTime = randrange(2, self._rangeTimeBetComments)
                commentArea = self._rugratSession.driver.ensure_element_by_class_name(
                    "Ypffh"
                )
                commentArea.click()
                commentArea = self._rugratSession.driver.ensure_element_by_class_name(
                    "Ypffh"
                )

                if self.isInternetOn() == 0:
                    continue

                commentArea.send_keys(self._listOfComments[index])
                commentArea.submit()
                sleep(sleepTime)

            except KeyboardInterrupt as interrupted:
                try:
                    print(interrupted)
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
