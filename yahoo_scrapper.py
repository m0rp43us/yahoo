from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import datetime
from dateutil.relativedelta import relativedelta
import glob, os
import csv
import psycopg2
import selenium.webdriver.support.ui as ui
import selenium
from goto import with_goto
import requests

ticker = 'TSLA'
yahoo = 'https://finance.yahoo.com/quote/TSLA/history?p='+ticker

WINDOW_SIZE = "1920,1080"
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--incognito")
firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=%s" % WINDOW_SIZE)

#webdriver config & settings
fp = webdriver.FirefoxProfile("/home/morpheus/.mozilla/firefox/")
fp.set_preference("browser.download.panel.shown", False)

#initianting browser
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),firefox_profile=fp)
browser.maximize_window()
link = a = browser.get(yahoo)
#html = BeautifulSoup(browser.page_source)
containers = browser.find_elements_by_xpath('//tr[@class="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"]')
for element in containers:
    data = element.find_elements_by_xpath('//td')
    for i in data:
        print(i.text)
#print(html)





