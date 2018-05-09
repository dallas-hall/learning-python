import re
print('@@@ String Substitution @@@')
print('[INFO] This can be seen at https://www.regular-expressions.info/backref.html')
print('You need to use the regex.sub(replacement, source_string) to get this to work. This can also use back references.')
regex = re.compile(r'Agent \w+')
start_string = 'Agent Alice gave the secret documents to Agent Bob.'
print(regex.sub('REDACTED', start_string))
regex = re.compile(r'Agent (\w)\w*')
start_string = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
print(regex.sub(r'\1***', start_string))