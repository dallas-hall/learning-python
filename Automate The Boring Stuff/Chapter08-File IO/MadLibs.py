#!/bin/python3
# Mad Libs is a game to replace multiple words (e.g. nouns, verbs, and adjectives) in a sentence with user provided words - https://en.wikipedia.org/wiki/Mad_Libs
import re

sentences = [
	'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
]
filePath = 'tmp/madlibs-output.txt'
file = open(filePath, 'w')

print('Enter an adjective.')
inputAdjective = input()
print('Enter a verb.')
inputVerb = input()
print('Enter a noun.')
inputNoun = input()

reAdjective = re.compile(r'\bADJECTIVE\b')
reVerb = re.compile(r'\bVERB\b')
reNoun = re.compile(r'\bNOUN\b')

for i in range(len(sentences)):
	currentSentence = reAdjective.sub(inputAdjective, sentences[i])
	currentSentence = reVerb.sub(inputVerb, currentSentence)
	currentSentence = reNoun.sub(inputNoun, currentSentence)
	print(currentSentence)
	file.write(currentSentence)

file.close()


