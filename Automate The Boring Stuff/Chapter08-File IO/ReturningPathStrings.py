import os

print('The current working directory is:\n' + os.getcwd())
print('\nPath without file returned via os.path.dirname() is:\n' + os.path.dirname(os.getcwd()))
print('\nPath with file returned via os.path.dirname() is:\n' + os.path.dirname(os.getcwd() + '/OSPathSupport.py'))
print('\nPath without file returned via os.path.basename() is:\n' + os.path.basename(os.getcwd()))
print('\nPath with file returned via os.path.basename() is:\n' + os.path.basename(os.getcwd() + '/OSPathSupport.py'))