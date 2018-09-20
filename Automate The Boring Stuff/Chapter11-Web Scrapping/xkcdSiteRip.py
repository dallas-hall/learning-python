#!/usr/bin/python3

import requests, os, sys, bs4, logging, re
from pathlib import Path

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
logging.info('Starting xkcdSiteRip.py')


def create_folder(path):
	if check_folder_exists(path):
		logging.warning('create_folder - Folder already exists, nothing done. ')
	else:
		if Path.is_absolute(Path(path)):
			Path.mkdir(Path(path))
		else:
			path = get_absolute_path(path)
			Path.mkdir(path)
		logging.debug('create_folder using\n' + str(path))


def check_folder_exists(path):
	if not Path.is_absolute(Path(path)):
		path = get_absolute_path(path)
		logging.debug('check_folder_exists - Converted to absolute path using')
	if Path.exists(Path(path)):
		return True
	else:
		return False


def get_absolute_path(path):
	if Path.is_absolute(Path(path)):
		return path
	else:
		logging.debug('get_absolute_path - Returning\n' + str(Path.cwd() / path))
		return runtime_path / path


def change_folder(path):
	if Path.is_absolute(Path(path)):
		os.chdir(path)
	else:
		path = get_absolute_path(path)
		os.chdir(str(path))
	logging.debug('change_folder using\n' + str(path))


# Setup variables
runtime_path = Path.cwd()
relative_path = 'xkcd'
absolute_path = get_absolute_path(relative_path)
url = 'https://xkcd.com'

# Setup file I/O
if not check_folder_exists(absolute_path):
	create_folder(absolute_path)
change_folder(absolute_path)

# xkcd start and ending urls end with #
while not url.endswith('#'):
	# Connect to website & check response code
	response = requests.get(url)
	try:
		response.raise_for_status()
	except Exception as e:
		logging.fatal('raise_for_status() - Exception was thrown for any response errors. Program exiting.')
		exit(1)

	# Get and parse HTML
	html = bs4.BeautifulSoup(response.text, 'lxml')
	#print(html.prettify())
	current_comic = html.select('#comic')
	print(current_comic)
	back_button = html.select('#middleContainer .comicNav li a')
	print(back_button[1])

	url = '#'

logging.info('Exiting xkcdSiteRip.py - all comics downloaded.')
