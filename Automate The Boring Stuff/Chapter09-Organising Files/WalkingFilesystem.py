import os
from pathlib import Path

sourcePath = str(Path.cwd()) + '/tmp'
os.chdir(sourcePath)
print(Path.cwd())
directoryName = 'dir-'
filename = 'file-'

# Create 3 directories
for i in range(3):
	currentPath = Path(sourcePath + '/' + directoryName + str(i + 1))
	if Path.exists(currentPath):
		if i == 0:
			print('[INFO] Cleaning up from previous run.')
		os.chdir(str(currentPath))
		# delete files first
		for currentFile in os.listdir(str(currentPath)):
			print('Deleting file ' + str(currentPath / currentFile))
			Path.unlink(currentPath / currentFile)
		# delete directory
		Path.rmdir(currentPath)

for i in range(3):
	currentPath = Path(sourcePath + '/' + directoryName + str(i + 1))
	if i == 0:
		print('[INFO] Creating directories and files.')
	Path.mkdir(currentPath)
	os.chdir(str(currentPath))
	for j in range(3):
		currentFilename = filename + str(j + 1)
		currentFile = open(currentFilename, 'w')
		currentFile.write(str(j) + '\n')
		currentFile.close()
		print(str(currentPath) + '/' + currentFilename)

