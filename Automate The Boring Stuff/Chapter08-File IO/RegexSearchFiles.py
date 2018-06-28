import re, os


print('Enter the search string.')
searchString = input()
searchPath = 'tmp/'
regex = re.compile(searchString)

# List all files in the directory
allFiles = os.listdir(searchPath)
for i in range(len(allFiles)):
	# Create an absolute path by joining the relative path and filename
	currentPath = os.path.abspath(os.path.join(searchPath, allFiles[i]))
	currentFile = open(currentPath, 'r')
	currentFileContents = currentFile.read()
	match = regex.findall(currentFileContents)
	if match:
		print("'" + searchString + "' was found " + str(len(match)) + " times in " + currentPath)
		print('The matches were: ' + str(match))

