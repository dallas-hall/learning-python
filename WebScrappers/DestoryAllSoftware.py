'''
This script will connect to https://www.destroyallsoftware.com/screencasts/catalog and get all of the links for each
season and then create a directory and download them.

A lot of these concepts were taken from https://automatetheboringstuff.com/chapter11/
'''

# @@@ IMPORTS @@@
from bs4 import BeautifulSoup
import requests, os, re

# @@@ GLOBAL VARIABLES @@@
# ### Internet ###
url = "https://www.destroyallsoftware.com/screencasts/catalog"
# get request to the website
response = requests.get(url)
# get the page source code
soup = BeautifulSoup(response.content)

# ### Catalogue ###
catalogue_episode_counts = [4, 6, 10, 18, 18, 18, 18, 18]
catalogue_season_names = []
catalogue_all_episodes = []
season_episodes = {}

# ### Filesystem ###
download_path = '/home/blindcant/Downloads/'

# @@@ SCRIPT @@@
# ### Scrape Data ###
# *** Get Season Names ***
# find all a tags that aren't links
for name_element in soup.find_all('a', href=False):
	# grab attribute inside the tag
	current_attribute = name_element['name']
	catalogue_season_names.append(current_attribute)

# *** Get Episode Links ***
# search for a particular class
soup.select('.container season')
# find all a tags with links
for link_element in soup.find_all('a', href=True):
	# grab the link
	current_link = link_element['href']
	if str(current_link).startswith('/screencasts/catalog/'):
		catalogue_all_episodes.append('https://www.destroyallsoftware.com' + current_link)

# ### Create Links ###
# *** Combine Names & Links ***
starting_number = 0
for i in range(len(catalogue_episode_counts)):
	print('Episode count: ' + str(catalogue_episode_counts[i]))
	if i == 0:
		print('Episode slice: 0:' + str(catalogue_episode_counts[i]))
		print(catalogue_all_episodes[0:catalogue_episode_counts[i]])

		# slice the list from 0 to the end of the first catalogue
		current_season_episodes = catalogue_all_episodes[0:catalogue_episode_counts[i]]

		# update the starting number for the next iteration, for the first time the catalogue's end number is fine
		starting_number = catalogue_episode_counts[i]

		# add the season name and episodes to the dictionary
		season_episodes[catalogue_season_names[i]] = current_season_episodes
	else:
		print('Episode slice: ' + str(starting_number) + ':' + str(starting_number + catalogue_episode_counts[i]))
		print(catalogue_all_episodes[starting_number:starting_number + catalogue_episode_counts[i]])

		# slice the list from the starting number to the end of the current catalogue, which is starting number + amount of episodes
		current_season_episodes = catalogue_all_episodes[starting_number:starting_number + catalogue_episode_counts[i]]

		# update the starting number for the next iteration, which is starting number + episode count
		starting_number = starting_number + catalogue_episode_counts[i]

		# add the season name and episodes to the dictionary
		season_episodes[catalogue_season_names[i]] = current_season_episodes

# ### Download Files ###
# *** Create Folders ***
print('Creating download folders.')
# change to the download directory and check if the base folder exists, create it if it doesn't
os.chdir(download_path)
if not os.path.exists(download_path + 'Destroy_All_Software'):
	os.mkdir('Destroy_All_Software')
base_download_path = download_path + 'Destroy_All_Software/'
os.chdir(base_download_path)

# Go through all the key and value pairs. Need k, v here otherwise a tuple is returned
# Check if the sub-folders exist, create them if not
for k, v in season_episodes.items():
	# use the key to create the download path
	season_path = re.sub('-', '_', str(k))
	print(season_path)
	if not os.path.exists(season_path):
		os.mkdir(season_path)

# *** Get Files ***
# go through each key which has the season names
for k, v in season_episodes.items():
	season_path = re.sub('-', '_', str(k))
	season_download_path = base_download_path + season_path
	os.chdir(season_download_path)
	print('Current path is: ' + season_download_path)
	# go through each value pair which has the season episode urls
	for i in range(len(v)):
		# order the files using the websites order
		if i < 9:
			current_file_number = '0' + str(i + 1) + '-'
		else:
			current_file_number = str(i + 1) + '-'

		# create the filename with numbered prefix
		current_filename = current_file_number + re.sub('-', '_', re.sub(r'^.*/', '', str(v[i])) + '.mp4')

		# create the download rul
		current_download_url = str(v[i]) + '/download?resolution=1080p'

		# download the file and print some crap
		print('Reading & downloading: ' + current_download_url)
		response = requests.get(current_download_url)
		print('Writing to file: ' + current_filename)

		# save the file
		current_file = open(current_filename, 'wb')
		for chunk in response.iter_content(100000):
			current_file.write(chunk)
		current_file.close()

