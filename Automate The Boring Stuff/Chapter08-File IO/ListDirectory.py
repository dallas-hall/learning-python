import os

path = '/home/dhall/tmp'
result = os.listdir(path)
print('Listing the files inside of ' + path)
for i in range(len(result)):
	print(result[i])