import re

print('@@@ Start String @@@')
start_string = 'hahahahaha'
html = '<p>Some text in a <i>pargraph</i>.</p>'
print(start_string)

print('\n@@@ Greedy Matching @@@')
print('This is the default behaviour.')
regex = re.compile(r'(ha){3,5}')
match_object = regex.search(start_string)
print(regex.pattern + ' found ' + match_object.group())
regex = re.compile(r'(ha){,5}')
match_object = regex.search(start_string)
print(regex.pattern + ' found ' + match_object.group())
regex = re.compile(r'<.*>')
match_object = regex.search(html)
print(regex.pattern + ' found ' + match_object.group())

print('\n@@@ Non-Greedy Matching @@@')
regex = re.compile(r'(ha){3,5}?')
match_object = regex.search(start_string)
print(regex.pattern + ' found ' + match_object.group())
regex = re.compile(r'(ha){3,}?')
match_object = regex.search(start_string)
print(regex.pattern + ' found ' + match_object.group())
regex = re.compile(r'<.*?>')
match_object = regex.search(html)
print(regex.pattern + ' found ' + match_object.group())