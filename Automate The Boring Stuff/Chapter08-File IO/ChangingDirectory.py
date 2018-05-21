import os

print('pwd is : ' + os.getcwd())
print('Changing to /home/dhall/')
os.chdir('/home/dhall')
print('pwd is : ' + os.getcwd())
print('Changing to /home/root/ which doesn\'t exist - a FileNotFoundError will occur.')
os.chdir('/home/root')