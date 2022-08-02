#!/usr/bin/python3

import logging, random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
keys_string = ['UP', 'DOWN', 'LEFT', 'RIGHT']
turns = 32

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting Play2048.py')

logging.debug('Loading browser.')
# geckodriver needs to be installed from https://github.com/mozilla/geckodriver/releases and locatable within $PATH
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(3)
html = browser.find_element_by_tag_name('html')

logging.debug('Sending keys ' + str(turns) + ' times.')
for i in range(turns):
	prn = random.randint(0, len(keys) - 1)
	logging.debug('prn and key is ' + str(prn) + ' ' + keys_string[prn])
	html.send_keys(keys[prn])
	time.sleep(.250)
