aList = ['one', 'two', 'three']
print('@@@ Joining @@@')
print('### List ###')
print(aList)
# this is useful for joining a list into one string with a delimiter
aListAsAString = ', '.join(aList)
print('### String ###')
print(aListAsAString)
print('; '.join(aList))
print('\t '.join(aList))
print('\n@@@ Splitting @@@')
print('Splitting \'' + aListAsAString + '\' using , ')
print(aListAsAString.split(','))
