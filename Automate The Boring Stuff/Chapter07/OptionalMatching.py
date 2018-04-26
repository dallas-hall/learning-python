import re

# 0:1 Match
print("@@@ 0:1 Match @@@")
regex = re.compile(r'Bat(wo)?man')
match_object = regex.search('The adventures of Batman & Robin.')
if match_object:
	print(match_object.group())
else:
	print(regex + ' wasn\'t found.')

match_object = regex.search('The adventures of Wonder Woman & Batwoman.')
if match_object:
	print(match_object.group())
else:
	print(regex + ' wasn\'t found.')

# 0:Many Match
print("\n@@@ 0:Many Match @@@")
regex = re.compile(r'version [0-9]*')
match_object = regex.search('This isn\'t a version.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

match_object = regex.search('This is version 1.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

match_object = regex.search('This is a version 12.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

# same as above
regex = re.compile(r'version [0-9]{0,}')
match_object = regex.search('This isn\'t a version.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

match_object = regex.search('This is version 1.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

match_object = regex.search('This is a version 12.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

# 1:Many Match
print("\n@@@ 1:Many Match @@@")
regex = re.compile(r'version [0-9]+')
match_object = regex.search('This isn\'t a version.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

match_object = regex.search('This is version 1.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

match_object = regex.search('This is a version 12.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

# same as above
regex = re.compile(r'version [0-9]{1,}')
match_object = regex.search('This isn\'t a version.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

match_object = regex.search('This is version 1.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')

match_object = regex.search('This is a version 12.')
if match_object:
	print(match_object.group())
else:
	print(regex.pattern + ' wasn\'t found.')