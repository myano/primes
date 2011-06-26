#!/usr/bin/python

import math

def Is_Prime(p):
	''' 
	This function determines if a given number 'p' is a prime number or not. 
	'''
	p=int(abs(p))
	x=math.floor(math.sqrt(p))
	a=3
	z=x
	if p == 0:
		return False
	elif p == 1:
		return False
	elif p == 2:
		return True
	elif p % 2 == 0:
		return False
	elif p >= 9:
		if z % 2 == 0:
			z+=1
		while z >= 3:
			if p % z == 0:
				return False
			if p % a == 0:
				return False
			z-=2
			a+=2
	return True
			
if __name__ == '__main__':
	print getattr(Is_Prime,'__doc__')
	#num=raw_input("What number do you want to test? (To see if it is a prime?): ")
	#num=1746860020068409
	num=982451653
	num=int(num)
	if Is_Prime(num) == True:
		print "The number, ", num, " is a prime number!"
	else:	
		print "The number, ", num, " is a composite number!"
