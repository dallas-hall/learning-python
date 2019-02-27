#!/usr/bin/python3

import logging, os, time, pprint
from pathlib import Path, PurePath

# Define logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
logging.info('Starting WalkingFileSystem2.py')
logging.warning('Doesn\'t recursively go into subdirectories.')
time.sleep(0.001)


# Functions
def get_absolute_paths_with_os(directory):
	return [os.path.join(directory, file) for file in os.listdir(directory)]


def get_absolute_paths_with_pathlib(directory):
	return [PurePath.joinpath(directory, file) for file in Path(directory).iterdir()]


# Script body
pp = pprint.PrettyPrinter(width=128)
logging.info('Print absolute paths with os')
time.sleep(0.004)
print(pp.pprint(get_absolute_paths_with_os(os.getcwd())))

logging.info('Print absolute paths with pathlib')
time.sleep(0.004)
print(pp.pprint(get_absolute_paths_with_os(Path.cwd())))
