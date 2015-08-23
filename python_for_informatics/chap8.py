""" This program is for Exercises 1 of Chapter 8 """

def chop(list):
	length = len(list)
	del list[length-1]
	del list[0]

def middle(list):
	length = len(list)
	answer = list[1:length-1]
	return answer
