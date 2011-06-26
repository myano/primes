#!/usr/bin/python

import sys
import math
import gap_prime
import generateprimes

def generate_list(k):
	k=int(k)
	p=2
	while p <= k:
		y=gap_prime.do_check(p)
		if y==False:
			print p, ":", y
		#print p, ":", y
		p+=1
		

if __name__ == '__main__':
	again=True
	while again==True:
		num=raw_input("What number do you want to generate a list, testing the Prime-couting function? : ")
		print generate_list(num)
		goagain=raw_input("\nWould you like to try another number? (yes/no) ")
		if goagain == "yes" or goagain == "y":
			again=True
		else:
			again=False
		print "\n"
