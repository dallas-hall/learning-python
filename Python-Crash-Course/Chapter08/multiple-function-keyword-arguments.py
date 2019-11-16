#!/usr/bin/python3
import logging, sys, os, time
from pprint import pprint

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)


# Allows the passing of an arbitrary number of key value pairs.
# Typically written as **kwargs
def build_profile(username, password, **user_profile):
	# Create an empty dictionary named user_profile and add everything to it
	# These passed in arguments need to be added manually, all **kwargs are added automatically
	user_profile['username'] = username
	user_profile['password'] = password
	return user_profile

user_profiles = []
user_profiles.append(build_profile("john", "abc123", email="john79@gmail.com", subscribe=True, interests=["sport", "health"]))
user_profiles.append(build_profile("jane", "qwerty", email="jane88@gmail.com", subscribe=False, interests=["shopping", "travel"]))
pprint(user_profiles)