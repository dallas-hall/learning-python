import requests, logging
# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')

result = requests.get('https://automatetheboringstuff.com/files/rj.txt')
logging.debug(print(type(result)))
logging.debug('Status code:\n' + str(result.status_code))
logging.debug('Header:\n' + str(result.headers))
logging.debug('Encoding:\n' + str(result.encoding))
logging.debug('Request:\n' + str(result.request))
logging.debug('Line amount:\n' + str(len(result.text)))
logging.debug('Sample text:\n' + str(result.text[:250]))
