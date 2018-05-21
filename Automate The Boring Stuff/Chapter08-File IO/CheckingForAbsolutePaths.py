import os

path = os.path.abspath('.')
print('Absolute path using os.path.abspath()is:\n' + path)
print('\nAbsolute path using os.getcwd()is:\n' + os.getcwd())
path = os.path.abspath('./tmp')
print('\nAbsolute path using os.path.abspath()is:\n' + path)
print('\nAbsolute path using os.getcwd()is:\n' + os.getcwd())
print('\nIs . an aboslute path? ' + str(os.path.isabs('.')))
print('\nIs os.path.abspath(\'.\') an aboslute path? ' + str(os.path.isabs(os.path.abspath('./tmp'))))