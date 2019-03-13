import os

path1 = '/home/dhall'
path2 = '/home/blindcant'
file1 = '.vimrc'
file2 = '.bashrc'
print('[INFORMATION] Using os.path.exists() to check path validity.')
print('Is ' + path1 + ' a valid path? ' + str(os.path.exists(path1)))
print('Is ' + path2 + ' a valid path? ' + str(os.path.exists(path2)))
print('Is ' + path1 + '/' + file1 + ' a valid path? ' + str(os.path.exists(path1 + '/' + file1)))
print('Is ' + path1 + '/' + file2 + ' a valid path? ' + str(os.path.exists(path1 + '/' + file2)))
print('Is ' + path2 + '/' + file1 + ' a valid path? ' + str(os.path.exists(path2 + '/' + file1)))
print('Is ' + path2 + '/' + file2 + ' a valid path? ' + str(os.path.exists(path2 + '/' + file2)))
print('\n[INFORMATION] Using os.path.isdir() to check for directories.')
print('Is ' + path1 + ' a directory? ' + str(os.path.isdir(path1)))
print('Is ' + path2 + ' a directory? ' + str(os.path.isdir(path2)))
print('Is ' + path1 + '/' + file1 + ' a directory? ' + str(os.path.isdir(path1 + '/' + file1)))
print('Is ' + path1 + '/' + file2 + ' a directory? ' + str(os.path.isdir(path1 + '/' + file2)))
print('Is ' + path2 + '/' + file1 + ' a directory? ' + str(os.path.isdir(path2 + '/' + file1)))
print('Is ' + path2 + '/' + file2 + ' a directory? ' + str(os.path.isdir(path2 + '/' + file2)))
print('\n[INFORMATION] Using os.path.isfile() to check for directories.')
print('Is ' + path1 + ' a file? ' + str(os.path.isfile(path1)))
print('Is ' + path2 + ' a file? ' + str(os.path.isfile(path2)))
print('Is ' + path1 + '/' + file1 + ' a file? ' + str(os.path.isfile(path1 + '/' + file1)))
print('Is ' + path1 + '/' + file2 + ' a file? ' + str(os.path.isfile(path1 + '/' + file2)))
print('Is ' + path2 + '/' + file1 + ' a file? ' + str(os.path.isfile(path2 + '/' + file1)))
print('Is ' + path2 + '/' + file2 + ' a file? ' + str(os.path.isfile(path2 + '/' + file2)))