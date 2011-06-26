#!/usr/bin/python

import sys

def fib(n):
	if n >= 0:
		b=n*(fib(n-1))
		#fib(n-1)
		return b
		
if __name__ == '__main__':
	n=raw_input('Please enter how many fibonacci numbers you would like: ')
	n=int(n)
	print fib(n)
