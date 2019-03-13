import requests, logging, os
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
download_path = str(Path.cwd()) + '/tmp'
if not Path.exists(Path(download_path)):
	Path.mkdir(Path(download_path))
os.chdir(download_path)

url = 'https://automatetheboringstuff.com/files/rj.txt'
logging.info('Requesting the file @\n' + url)
response = requests.get(url)

logging.info('Reading response.')
response.raise_for_status()

logging.info('Response okay, downloading file.')
# Need to open the file in binary mode to ensure the correct bytes are downloaded, otherwise incorrect character set translation will happen.
download_file = open(download_path + '/Romeo_and_Juliet.txt', 'wb')
# The number is in bytes (current 100,000 bytes or 1/10 of a Megabyte)
for chunk in response.iter_content(100000):
	download_file.write(chunk)
download_file.close()
logging.info('File downloaded.')