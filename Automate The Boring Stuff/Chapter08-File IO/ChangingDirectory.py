import os

print('pwd is:\n' + os.getcwd())
print('\nChanging to /home/dhall/')
os.chdir('/home/dhall')
print('pwd is:\n' + os.getcwd())
print('\nChanging to /home/root/ which doesn\'t exist - a FileNotFoundError will occur.')
os.chdir('/home/root')