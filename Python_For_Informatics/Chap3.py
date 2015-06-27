# This program is for Exercises 1 & 2 of Chapter 3

prompt1 = 'Enter Hours: '
prompt2 = 'Enter Rate: '

input1 = raw_input(prompt1)
input2 = raw_input(prompt2)

try:
	hours = float(input1)
	rate = float(input2)
	
	if rate<0:
		print 'Enter positive number for Rate'
	else:
		if rate>=0 and hours>=0 and hours<=40:
			pay1 = hours*rate
			print pay1
		else:
			if rate>=0 and hours>40:
				pay2 = (40*rate)+((hours-40)*(rate*1.5))
				print pay2
			else:
				if rate>=0 and hours<0:
					print 'Enter positive number for Hours'
except:
	print 'You must enter numbers for both Hours & Rate'

# This program is for Exercise 3 of Chapter 3

prompt = 'Enter Test Score: '

input = raw_input(prompt)

try:
	score = float(input)

	if score>=0 and score<0.6:
		print 'F'
	elif score>=0.6 and score<0.7:
		print 'D'
	elif score>=0.7 and score<0.8:
		print 'C'
	elif score>=0.8 and score<0.9:
		print 'B'
	elif score>=0.9 and score<=1.0:
		print 'A'
	elif score<0 or score>1:
		print 'Bad Score'
except:
	print 'Bad Score'
