import re

regex = re.compile(r'Bat(man|mobile|copter|shark)')
match = regex.search('The Batmobile lost a wheel, Batman cried.')
for i in range(match.lastindex + 1):
	print(match.group(i))

# because of the capture group it only returns the text inside the capture group
match = regex.findall('The Batmobile lost a wheel, Batman cried.')
print(match)

source_string = 'Cell: 415-555-9999 Work: 212-555-0000'
# return only if the start of the string matches the pattern
regex = re.compile(r'\d{3}-\d{3}-\d{4}')
match = regex.match(source_string)
if match:
	print(match.group())
else:
	print(regex.pattern + ' did not match the start of the string.')
# return the first match in the string
match = regex.search(source_string)
print(match.group())
# return all matches
match = regex.findall(source_string)
print(match)
regex = re.compile(r'(\d{3})-\d{3}-\d{4}')
# add a capture group to show how only the matches inside the capture group are returned.
match = regex.findall(source_string)
print(match)
