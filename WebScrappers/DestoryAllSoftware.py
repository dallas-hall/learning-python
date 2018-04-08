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
os.chdir(download_path)
if not os.path.exists(download_path + 'Destroy_All_Software'):
	os.mkdir('Destroy_All_Software')
os.chdir(download_path + 'Destroy_All_Software')

# need k, v here otherwise a tuple is returned
for k, v in season_episodes.items():
	if not os.path.exists(download_path + 'Destroy_All_Software/' + str(k)):
		os.mkdir(str(k))

# *** Get Files ***
for k, v in season_episodes.items():
	print(download_path + 'Destroy_All_Software/' + str(k))
	current_path = download_path + 'Destroy_All_Software/' + str(k)
	os.chdir(current_path)
	for i in range(len(v)):
		current_filename = re.sub(r'^.*/', '', str(v[i])) + '.mp4'
		current_download_path = str(v[i]) + '/download?resolution=1080p'
		print('Reading & downloading: ' + current_download_path)
		response = requests.get(current_download_path)
		print('Writing to file: ' + current_filename)
		current_file = open(current_filename, 'wb')
		for chunk in response.iter_content(100000):
			current_file.write(chunk)
		current_file.close()

