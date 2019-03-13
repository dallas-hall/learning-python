#!/usr/bin/python3

import requests, sys, webbrowser, bs4, logging, re

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')

logging.info('Starting GoogleSearches.py')
# Setup the Google query
url = 'https://www.google.com.au/search?q='
query_string = ' '.join(sys.argv[1:])
# Submit query to Google
logging.info('Googling -> ' + query_string)
response = requests.get(url + query_string)
try:
	response.raise_for_status()
except Exception as e:
	logging.fatal('raise_for_status() - Exception was thrown for any response errors. Program exiting.')
	exit(1)

# Get and parse HTML
html = bs4.BeautifulSoup(response.text, 'lxml')
search_result = html.select('#search')
links = html.select('.r a')

# Open top 5 links
for i in range(5):
	webbrowser.open('https://google.com' + links[i].get('href'))



