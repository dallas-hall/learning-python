import os

path = os.path.relpath('.')
print('Relative path using os.path.relpath() is:\n' + path)
print('\nAbsolute path using os.getcwd() is:\n' + os.getcwd())
path = os.path.relpath('./tmp')
print('\nRelative path using os.path.relpath() is:\n' + path)
print('\nAbsolute path using os.getcwd() is:\n' + os.getcwd())
print('\nIs . an aboslute path? ' + str(os.path.isabs('.')))
print('\nIs os.path.abspath(\'.\') an aboslute path? ' + str(os.path.isabs(os.path.abspath('./tmp'))))