#! python3
import random
import pprint

outputPath = 'tmp/'
quizAmount = 10

# create a dictionary (map) of states and their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
	'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
	'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
	'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
	'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
	'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
	'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
	'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
	'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
	'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
	'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
	'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
	'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
	'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
	'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
	'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
	'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for currentQuizNumber in range(quizAmount):
	# Create the quiz and answer key files.
	if currentQuizNumber + 1 < 10:
		currentQuizQuestionFile = open(outputPath + 'Capitals_Quiz_Questions_0%s.txt' % (currentQuizNumber + 1), 'w')
		currentQuizAnswerFile = open(outputPath + 'Capitals_Quiz_Answers_0%s.txt' % (currentQuizNumber + 1), 'w')
	else:
		currentQuizQuestionFile = open(outputPath + 'Capitals_Quiz_Questions_%s.txt' % (currentQuizNumber + 1), 'w')
		currentQuizAnswerFile = open(outputPath + 'Capitals_Quiz_Answers_%s.txt' % (currentQuizNumber + 1), 'w')

	# Write out the header for the quiz.
	currentQuizQuestionFile.write('Name:\n\nDate:\n\nClass:\n\n')
	currentQuizQuestionFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (currentQuizNumber + 1))
	currentQuizQuestionFile.write('\n\n')

	# Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)

	# the magic number 50 is from the 50 states
	for questionNumber in range(50):
		# Get right answer by accessing the dictionary
		correctAnswer = capitals[states[questionNumber]]
		# Get the wrong answers by getting all answers and removing the right answer
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		# Get 3 random wrong answers
		wrongAnswers = random.sample(wrongAnswers, 3)
		# Create 4 answer options and shuffle them
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		# Write the question and the answer options to the quiz file.
		currentQuizQuestionFile.write('%s. What is the capital of %s?\n' % (questionNumber + 1, states[questionNumber]))
		for i in range(4):
			currentQuizQuestionFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
			currentQuizQuestionFile.write('\n')

		# Write the answer key to a file.
		currentQuizAnswerFile.write('%s. %s\n' % (questionNumber + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

	# Close the file resources
	currentQuizQuestionFile.close()
	currentQuizAnswerFile.close()
