#!/usr/local/bin/python

import Is_Prime

def numlist(h):
	''' This function will generate a list of numbers starting at 2, and working up to the number you enter.
	It will list if it is a prime number or if it is not.
	'''
	#listofprimefactors=[]
	list_primes=[]
	#for n in range(2, h+2):
	n=2
	line=0
	while n <= (h):
		if Is_Prime.Is_Prime(n)==True:
			list_primes.append(n)
		n+=1

	print "'",len(list_primes),"'th prime number:",list_primes[-1]


if __name__ == '__main__':
	print 
	usernum=raw_input("What is the max number you would like to gernerate up to? ")
	usernum=int(usernum)
#	print Is_Prime.Is_Prime(usernum)
	print numlist(usernum)
