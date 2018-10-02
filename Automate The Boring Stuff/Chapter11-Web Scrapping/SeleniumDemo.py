#!/usr/bin/python3

import logging
from selenium import webdriver

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting SeleniumDemo.py')

logging.debug('Loading browser.')
# geckodriver needs to be installed from https://github.com/mozilla/geckodriver/releases and locatable within $PATH
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

logging.debug('Searching for an element on the page.')
try:
    elem = browser.find_element_by_class_name('jumbotron')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

logging.debug('Clicking an element on the page.')
linkElem = browser.find_element_by_link_text('Cracking Codes with Python')
linkElem.click() # follows the "Read It Online" link