# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 23:05:34 2018

@author: anustubh agnihotri
This script introduces students to the selenium webdriver and its basic functionality 
More details regarding selenium can be found at https://selenium-python.readthedocs.io/index.html

The steps for this script are as follows
1. pip install selenium to get the selenium module
2. download the selenium webdrive for Chrome/Firefox and save it in a local folder 
3. make sure webdrive matches your OS
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
#set working directory

os.chdir(r'C:/Users/Julia/OneDrive/Documents/Berkeley/2020-01_Spring/PS239T_Spring2020/07_webscraping')


##select the chrome webdriver
path_to_chromedriver = "C:/Users/Julia/OneDrive/Documents/Berkeley/2020-01_Spring/PS239T_Spring2020/07_webscraping/chromedriver_win32/chromedriver.exe"
chromeOptions = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path = path_to_chromedriver,port=0,chrome_options=chromeOptions, service_args=None, desired_capabilities=None, service_log_path=None)

    
# website to scrape
url = "http://www.python.org"

# launch the webdrive and get the url
browser.get(url)


# get a link and click on it

link = browser.find_element_by_link_text('Downloads')

link.click()

# explore the functionality 

browser.back()

# find an element 

elem = browser.find_element_by_name("q")

# interact with the web-page 
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)

# new way of finding element 

elem = browser.find_element_by_id("id-search-field")

elem.clear()
# interact with the web-page 
elem.send_keys("selenium a new way")
elem.send_keys(Keys.RETURN)


# wait 

#explicit 
time.sleep(12)

#go to a new url

url2='https://www.wikipedia.org/'

# a url that does not open
url_not_opening='https://revenueharyana.gov.in/'
#logging exceptions 

try:
    browser.get(url2)
except TimeoutException as ex:
    f = open('log.txt', 'a')
    f.write('Timeout Exception')    
    f.close()          

#due to the timeout exception your script does not crash
try:
    browser.set_page_load_timeout(10)
    browser.get(url_not_opening)
except TimeoutException as ex:
    f = open('log.txt', 'a')
    f.write('Timeout Exception')    
    f.close()      
    print('Time out')    
