""" This program is for Exercise 1 of Chapter 5 """

prompt = 'Enter a number: '

a = []

while True:
	response = raw_input(prompt)
	if response == 'done':
		break
	else:
		try:
			value = float(response)
			a.append(value)
		except:
			print 'Bad data'
			continue

total = sum(a)
length = len(a)
mean = total/length

print "Total:  ",total,"\n","Count:  ",length,"\n","Average:",mean

""" This program is for Exercise 2 of Chapter 5 """

prompt = 'Enter a number: '

a = []

while True:
	response = raw_input(prompt)
	if response == 'done':
		break
	else:
		try:
			value = float(response)
			a.append(value)
		except:
			print 'Bad data'
			continue

top_value = max(a)
bottom_value = min(a)

print "Maximum:",top_value,"\n","Minimum:",bottom_value
