#!/usr/bin/python

import sys
import random

print 'Fallout Mini-Game!'

#read in the dictionary
if len(sys.argv) != 2:
	sys.exit('Usage: fallout.py dictionary-name.txt')
	
f = open(sys.argv[1], 'r')

dic = []

for line in f:
	dic.append(line.strip())
	
#set difficulties
diff = -1
difficulties = {1 : (4, 4), 2 : (5, 7), 3 : (8, 10), 4 : (11, 14), 5 : (15, 15)}
while diff > 5 or diff < 0:
	diff = int(raw_input('Difficuty (1-5)? '))
numwords = difficulties[diff][1]
numletters = difficulties[diff][0]
numguesses = 4

# gets a random word from dic that has the lenth of word
words = []
for i in range(0, numwords):
	word = ''
	
	while len(word) != numletters:
		word = dic[random.randint(0, len(dic))]
		
	words.append(word)

#prints all words
for i in words:
	print i

#decide correct word
correct_word = words[random.randint(0, len(words)-1)]

print 'correct word is: ' + correct_word

guess = ''

while guess != correct_word and numguesses > 0:
	guess = raw_input('Guess (' + str(numguesses) + ' left)? ')
	
	if guess == correct_word:
		print 'WOOOOO!!!!!!!!!!!!!!!!'
		sys.exit(0)
	elif guess in words:
		matches = 0
		zipped = zip(guess, correct_word)
		for i,j in zipped:
			if i==j:
				matches += 1
				
		print str(matches) + '/' + str(numletters) + ' correct'

		numguesses -= 1
	else:
		print 'Guess a word from the list'

print 'boo'
sys.exit(0)
