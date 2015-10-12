""" This program is for Exercise 1 of Chapter 9 """

""" While this isn't precisely what's requested, I believe this solution goes slightly beyond what is asked of the reader """

import string

prompt1 = 'Enter the file name: '

target1 = raw_input(prompt1)

target_file = open(target1)

d = dict()

for line in target_file:
	line = line.split()
	for word in line:
		if word not in d:
			word = ''.join([c for c in word if c not in (',', '?')])
			d[word] = 1
		else:
			d[word] += 1

prompt2 = 'Enter word: '

target2 = raw_input(prompt2)

print 'The word',target2,'appears',d[target2],'times in words.txt.'
