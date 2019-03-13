"""
These two variables will be for the intersections of Market Street and 2nd Street, and Mission Street and 16th Street.

The data structure representing the stoplights at an intersection is a dictionary with keys 'ns' and 'ew', for the
stoplights facing north-south and east-west, respectively. The values at these keys will be one of the strings 'green',
 ' yellow', or 'red'.
"""
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key] = 'yellow'
		elif stoplight[key] == 'yellow':
			stoplight[key] = 'red'
		elif stoplight[key] == 'red':
			stoplight[key] = 'green'
		# Checks to make sure at least one of the stop lights is red.
		assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)


switchLights(market_2nd)
