import os

path1 = '/home/dhall'
path2 = '/home/blindcant'
file1 = '.vimrc'
file2 = '.bashrc'
print('\n[INFORMATION] Using os.path.isfile() to check for files.')
print('Is ' + path1 + ' a file? ' + str(os.path.isfile(path1)))
print('Is ' + path2 + ' a file? ' + str(os.path.isfile(path2)))
print('Is ' + path1 + '/' + file1 + ' a file? ' + str(os.path.isfile(path1 + '/' + file1)))
print('Is ' + path1 + '/' + file2 + ' a file? ' + str(os.path.isfile(path1 + '/' + file2)))
print('Is ' + path2 + '/' + file1 + ' a file? ' + str(os.path.isfile(path2 + '/' + file1)))
print('Is ' + path2 + '/' + file2 + ' a file? ' + str(os.path.isfile(path2 + '/' + file2)))