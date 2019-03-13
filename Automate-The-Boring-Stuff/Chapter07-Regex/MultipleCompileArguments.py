import re
print('@@@ Multiple re.compile() Arguments @@@')
print(r're.compile() can only accept a single secondary argument. So the bitwise or operator which is a pipe | is needed to separate the arguments.')
print(r'Here is an example showing how to use 3 secondary arguments at once with or logic.')
print(r're.compile(\'foo\', re.IGNORECASE | re.DOTALL | re.VERBOSE)')
