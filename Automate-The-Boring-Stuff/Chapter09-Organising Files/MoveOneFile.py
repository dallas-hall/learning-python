from pathlib import Path
import os, shutil

os.chdir('tmp/')
sourcePath = os.getcwd()
os.chdir('complete-copy/')
targetPath = os.getcwd()
filename = 'file-to-move'

print(targetPath)
print(filename)
print(sourcePath)


file = open(sourcePath + '/' + filename, 'w')
file.write(str(sourcePath))
file.write(str(filename) + '\n')
file.write(str(targetPath))
file.close()

print('[INFO] Moving ' + str(sourcePath) + '/' + filename + ' to\n' + str(targetPath))

# Don't need to supply the target filename unless you want to change it.
# Move will automatically overwrite existing files.
# The destination is a filename only, move cannot create folders and will error if it doesn't exist (FileNotFoundError)
shutil.move(sourcePath + '/' + filename, targetPath)

# Move back with Path
# The filename must be specified here.
Path.rename(Path(targetPath + '/' + filename), sourcePath + '/' + filename)
