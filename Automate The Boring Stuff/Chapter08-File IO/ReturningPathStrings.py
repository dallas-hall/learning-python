import os

path_only = str(os.getcwd())
path_and_file = str(os.getcwd() + '/OsSafePathSupport.py')

print('The current working directory is:\n' + path_only)
print('\nPath without file returned via os.path.dirname() is:\n' + os.path.dirname(path_only))
print('\nPath with file returned via os.path.dirname() is:\n' + os.path.dirname(path_and_file))
print('\nPath without file returned via os.path.basename() is:\n' + os.path.basename(path_only))
print('\nPath with file returned via os.path.basename() is:\n' + os.path.basename(path_and_file))
print('\nPath without file returned via os.path.split() is:\n' + str(os.path.split(path_only)))
print('\nPath with file returned via os.path.split() is:\n' + str(os.path.split(path_and_file)))