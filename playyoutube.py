from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class youtubeBot:
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox()

    def playvideo(self):
        url = self.url
        driver = self.driver
        driver.get(url)

