import os

path_only = str(os.getcwd())
path_and_file = str(os.getcwd() + '/OsSafePathSupport.py')
# In Linux the first element will be empty, in Windows this will be the drive letter.
print(path_only.split(os.path.sep))
print(path_and_file.split(os.path.sep))
