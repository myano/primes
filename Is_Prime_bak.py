#!/usr/bin/python

import math

def Is_Prime(p):
	''' This function determines if a given number 'p' is a prime number or not. '''
	p=int(abs(p))
	x=math.floor(math.sqrt(p)) #start at 2 for testing because all number are divisible by 1
	y=2
	a=3
	b=(x-1)
	z=x
	while z >= (x/2): # only needs to check up to the square root of the number p, because anything higher than p is not necessary.
		if p % z == 0: #if composite
			return False
		if p % y == 0:
			return False
		if p % a == 0:
			return False
		if b >1: 
			if p % b == 0:
				return False
		z-=1
		y+=1
		a+=2
		b-=2
	return True
			
if __name__ == '__main__':
	num=raw_input("What number do you want to test? (To see if it is a prime?): ")
	#num=1746860020068409
	#num=982451653
	num=int(num)
	if Is_Prime(num) == True:
		print "The number, ", num, " is a prime number!"
	else:	
		print "The number, ", num, " is a composite number!"
