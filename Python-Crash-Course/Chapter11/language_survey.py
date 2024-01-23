#!/usr/bin/env python3
import logging, sys, os, time
# To import this in PyCharm, right click the folder and mark as Sources Root
from survey import AnonymousSurvey

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.100)

# Create a question
question = "What langauge did you first learn to speak?"

# Call the constructor and pass the question
my_survey = AnonymousSurvey(question)

# Use the AnonymousSurvey object
while True:
	my_survey.show_question()
	response = input()
	my_survey.store_response(response)
	response = input("Do you want to continue? [y/n]")
	if response.lower() == "n":
		break

print("Thank you for taking the survey, the following responses were recorded.")
my_survey.show_results()
