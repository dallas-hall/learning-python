import shutil,os

os.chdir('tmp/')
targetPath = os.getcwd()
print(targetPath)
os.chdir('../../Chapter08-File IO/tmp')
sourcePath = os.getcwd()
print(sourcePath)
filename = 'cats.txt'
print(filename)

print('[INFO] Copying ' + sourcePath + '/' + filename + ' to\n' + targetPath)
# don't need to supply the target filename unless you want to change it
shutil.copy(sourcePath + "/" + filename, targetPath)