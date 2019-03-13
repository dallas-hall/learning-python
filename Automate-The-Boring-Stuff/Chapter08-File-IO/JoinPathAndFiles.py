import os

home_path = '/home/dhall/tmp/'
filenames = ['distros.txt', 'distros_and_nl.sed', 'distros_and_tbl.sed']
for i in range(len(filenames)):
	print(os.path.join(home_path, filenames[i]))
