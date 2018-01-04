# import the prn module
import random

# create a list of 8 ball questions
questions = ['Will I be happy?',
             'Am I smart?',
             'Do people think I smell?',
             'Do I like cheese?',
             'Am I booootiful?',
             'Why am I always tired?']

# create a list with 8 ball answers
answers = ['It is certain',
           'It is decidedly so',
           'Yes definitely',
           'Reply hazy try again',
           'Ask again later',
           'Concentrate and ask again',
           'My reply is no',
           'Outlook not so good',
           'Very doubtful']

# print 3 random questions & answers
for i in range(3):
    # use random to create a prn between 0 and the length of the list - 1
    print(questions[random.randint(0, len(questions) - 1)])
    print(answers[random.randint(0, len(answers) - 1)])
    print('\n')