import re

regex = re.compile(r'Bat(man|mobile|copter|shark)')
match = regex.search('The Batmobile lost a wheel, Batman cried.')
for i in range(match.lastindex + 1):
	print(match.group(i))

match = regex.findall('The Batmobile lost a wheel, Batman cried.')
print(match)