import requests, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')

logging.info('raise_for_status() - Nothing is done for a valid response.')
response = requests.get("http://www.google.com.au")
response.raise_for_status()

try:
	logging.error('raise_for_status() - Exception is thrown for any response errors.')
	response = requests.get("http://www.google.com.au/no-page-here-bro")
	response.raise_for_status()
except Exception as e:
	logging.info('Exception caught, continuing execution.')


logging.fatal('raise_for_status() - Exception is thrown for any response errors.')
response = requests.get("http://www.google.com.au/no-page-here-bro")
response.raise_for_status()
