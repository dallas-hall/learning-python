#!/usr/bin/python3

import logging, time
from selenium import webdriver


# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting GoogleMailFormFilling.py')

url = 'https://www.google.com/gmail/'

logging.debug('Loading browser.')
browser = webdriver.Firefox()
browser.get(url)

logging.debug('Searching for an element on the page.')

email_textfield = browser.find_element_by_id('identifierId')
time.sleep(1)
email_textfield.send_keys('email@gmail.com')

next_button = browser.find_element_by_id('identifierNext')
next_button.click()
time.sleep(2)

password_textfield = browser.find_element_by_css_selector("input[type='password']")
time.sleep(1)
password_textfield.send_keys('abc123')

next_button = browser.find_element_by_id('passwordNext')
next_button.click()

time.sleep(2)
password_textfield = browser.find_element_by_css_selector("input[type='password']")
time.sleep(1)
password_textfield.send_keys('abc123')
captcha_textfield = browser.find_element_by_id('ca')
time.sleep(1)
captcha_textfield.send_keys('captcha')

next_button = browser.find_element_by_id('passwordNext')
next_button.click()