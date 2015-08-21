""" This program is for Exercise 1 of Chapter 6 """

prompt = 'Enter a word: '

input = raw_input(prompt)

length = len(input)

index = length-1

while index >= 0:
	letter = input[index]
	print letter
	index = index - 1

""" Exercise 2 of Chapter 6 is non-programming """

""" This program is for Exercise 3 of Chapter 6 """

prompt1 = 'Enter your word: '
prompt2 = 'Enter the letter: '
	
word = raw_input(prompt1)
chosen = raw_input(prompt2)

def count_letter(word,chosen):
	count=0
	for letter in word:
		if chosen == letter:
			count = count + 1
	print count

count_letter(word,chosen)

""" This program is for Exercise 4 of Chapter 6 """

prompt1 = 'Enter your word: '
prompt2 = 'Enter the letter: '

input1 = raw_input(prompt1)
input2 = raw_input(prompt2)

word = str(input1)
letter = str(input2)

final_word = word.lower()
final_letter = letter.lower()

count = final_word.count(final_letter)

print 'The letter',final_letter,'appears',count,'times in',word

""" This program is for Exercise 5 of Chapter 6 """

str = 'X-DSPAM-Confidence: 0.4875'

index = str.find(':')

a = str[index+1:]
b = a.strip()

result = float(b)

print result

""" Exercise 6 of Chapter 6 is non-programming """
