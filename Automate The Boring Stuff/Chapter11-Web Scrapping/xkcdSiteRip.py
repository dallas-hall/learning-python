#!/usr/bin/python3

import requests, os, bs4, logging, re, datetime
from pathlib import Path

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
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


def get_number_prefix(n):
	r = int(re.sub(regex_remove_slash, '', n))
	if r >= 1 and r <= 9:
		return '0000' + str(r)
	elif r >= 10 and r <= 99:
		return '000' + str(r)
	elif r >= 100 and r <= 999:
		return '00' + str(r)
	elif r >= 1000 and r <= 9999:
		return '0' + str(r)
	else:
		return str(r)

def write_to_file(path, write_mode, message):
	file = open(path, write_mode)
	file.write(message)
	file.close()

# Setup variables
runtime_path = Path.cwd()
relative_path = 'xkcd'
absolute_path = get_absolute_path(relative_path)
start_url = 'https://xkcd.com'
next_comic_number = '/1/' # 1350 is the first comic that isn't a PNG file
url = start_url + next_comic_number
regex_match_non_filename = re.compile(r'^.*/')
metadata_file = 'comics_metadata.txt'
regex_remove_slash = re.compile(r'/+')


# Setup file I/O
if not check_folder_exists(absolute_path):
	create_folder(absolute_path)
change_folder(absolute_path)
write_to_file(str(absolute_path) + '/' + metadata_file, 'w', 'Downloading all comics from ' + url + ' @ ' + str(datetime.datetime.now()).split('.')[0] + '\n')

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
	# if debugging:
	# 	logging.debug(html.prettify())

	# Download the comic
	current_comic = html.select('#comic img')
	# Skip if it ins't an image file, some xkcd comics are not images.
	if len(current_comic) == 0:
		current_comic_number = re.sub(r'https://xkcd.com', '', url)
		current_comic_number_no_slashes = re.sub(r'/', '', current_comic_number)
		write_to_file(
			str(absolute_path) + '/' + metadata_file
			,'a'
			,'\nComic number ' + current_comic_number_no_slashes + ' not downloaded as it wasn\'t an image file.'
		)
		url = start_url + '/' + str(int(current_comic_number_no_slashes) + 1) + '/'
		continue

	current_file_number_prefix = get_number_prefix(next_comic_number)
	current_comic_filename = current_file_number_prefix + '_' + re.sub(r'_\(.*\)', '', re.sub(regex_match_non_filename, '', current_comic[0].get('src')))
	logging.debug('Current filename:\n' + current_comic_filename)
	current_comic_url = 'https:' + current_comic[0].get('src')
	logging.debug('Current URL:\n' + current_comic_url)
	response = requests.get(current_comic_url)
	try:
		response.raise_for_status()
	except Exception as e:
		logging.fatal('raise_for_status() - Exception was thrown for any response errors. Program exiting.')
		exit(1)

	# Need to open the file in binary mode to ensure the correct bytes are downloaded, otherwise incorrect character set translation will happen.
	download_file = open(str(absolute_path) + '/' + current_comic_filename, 'wb')
	# The number is in bytes (current 100,000 bytes or 1/10 of a Megabyte)
	for chunk in response.iter_content(100000):
		download_file.write(chunk)
	download_file.close()
	logging.info(current_comic_filename + ' downloaded.')

	# Get the next comic
	next_comic_number = html.select('#middleContainer .comicNav li a')[3].get('href')
	url = start_url + next_comic_number
	logging.debug('Next URL:\n' + url)

	# TODO: check for non-pictures - https://xkcd.com/1350/ is a problem because it isn't a picture

	# Write metadata
	current_comic_number = int(re.sub(r'/', '', next_comic_number)) - 1
	write_to_file(str(absolute_path) + '/' + metadata_file, 'a',  '\nDownloaded comic number ' + str(current_comic_number) + ' named ' + current_comic_filename + ' from ' + current_comic_url)

	#url = '#'

logging.info('Exiting xkcdSiteRip.py - all comics downloaded.')
