import os

path1 = '/home/dhall'
path2 = '/home/blindcant'
file1 = '.vimrc'
file2 = '.bashrc'
print('\n[INFORMATION] Using os.path.isdir() to check for directories.')
print('Is ' + path1 + ' a directory? ' + str(os.path.isdir(path1)))
print('Is ' + path2 + ' a directory? ' + str(os.path.isdir(path2)))
print('Is ' + path1 + '/' + file1 + ' a directory? ' + str(os.path.isdir(path1 + '/' + file1)))
print('Is ' + path1 + '/' + file2 + ' a directory? ' + str(os.path.isdir(path1 + '/' + file2)))
print('Is ' + path2 + '/' + file1 + ' a directory? ' + str(os.path.isdir(path2 + '/' + file1)))
print('Is ' + path2 + '/' + file2 + ' a directory? ' + str(os.path.isdir(path2 + '/' + file2)))