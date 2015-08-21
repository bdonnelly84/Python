""" This program is for Exercise 1 of Chapter 7 """

prompt = 'Enter the file name: '

target = raw_input(prompt)

target_file = open(target)

for line in target_file:
	line = line.strip()
	line = line.upper()
	print line

""" This program is for Exercise 2 of Chapter 7 """

prompt = 'Enter the file name: '

target = raw_input(prompt)

target_file = open(target)

count = 0
total = 0

for line in target_file:
	if line.startswith('X-DSPAM-Confidence: '):
		count = count + 1
		a = line[19:]
		b = a.strip()
		result = float(b)
		total = total + result
	else:
		continue

average = total/count

print 'Average spam confidence:',average

""" This program is for Exercise 3 of Chapter 7 """

prompt = 'Enter the file name: '

target = raw_input(prompt)

if target == 'na na boo boo':
	print 'NA NA BOO BOO TO YOU - You have been punk\'d!'
else:
	try:
		count = 0
		target_file = open(target)
		for line in target_file:
			count = count + 1
		print 'There are',count,'subject lines in',target
	except:
		print 'File could not be opended:',target
