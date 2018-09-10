import logging, requests, bs4, re

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
regex = re.compile(r'\s+')

url = 'http://www.bom.gov.au/places/qld/brisbane/'
response = requests.get(url)
try:
	response.raise_for_status()
except Exception as e:
	logging.fatal('raise_for_status() - Exception was thrown for any response errors. Program exiting.')
	exit(1)

# Get all html elements
html = bs4.BeautifulSoup(response.text, 'lxml')
# Extract the text from a specific HTML element using CSS selectors
city = html.select('h1')[0].getText()
# Use regex to replace multiple whitespace into 1 and remove leading/trailing whitespace
current_air_temp = 'Current ' + regex.sub(r' ', html.select('#summary-1 ul li')[0].getText()).strip()
recorded_min_temp = regex.sub(r' ', html.select('#summary-1 ul li')[1].getText()).strip()
recorded_max_temp = regex.sub(r' ', html.select('#summary-1 ul li')[2].getText()).strip()
rain = regex.sub(r' ', html.select('#summary-1 ul li')[3].getText()).strip()
forecast_text = regex.sub(r' ', html.select('.forecasts h2')[0].getText()).strip()
predicted_max_temp = 'Max ' + regex.sub(r' ', html.select('.forecast-summary dd')[1].getText()).strip()
predicted_weather = regex.sub(r' ', html.select('.forecast-summary dd')[2].getText()).strip()

print(city)
print(current_air_temp)
print(recorded_min_temp)
print(recorded_max_temp)
print(rain)
print(forecast_text)
print(predicted_max_temp)
print(predicted_weather)