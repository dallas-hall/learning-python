import os

path = '/home/dhall/tmp/distros.txt'
print('The size of ' + path + ' is:')
print(str(os.path.getsize(path)) + ' bytes')