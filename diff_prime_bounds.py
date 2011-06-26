#!/usr/local/bin/python

import sys
import Is_Prime
import math

def numlist(h):
	#listofprimefactors=[]
	list_primes=[]
	#for n in range(2, h+2):
	n=2 #org: 2
	line=0
	nth_prime=0 #org: 0
	counter_low=0
	counter_high=0
	print "'nth prime lowbound is: (lowbound) < prime < (highbound)"
	while n <= h:
		if Is_Prime.Is_Prime(n)==True: #if prime originally was "elif: x == n-1:"
			#list_primes.append(n)
			nth_prime+=1
			if nth_prime > 1:
				#print "'",nth_prime,"'th prime is :",n
	                        ln_n=(math.log(nth_prime))
	                        #print "nth_prime",nth_prime," ","ln_n:",ln_n
	                        ln_n_n=(math.log(ln_n))
	                        #print "ln_n_n", ln_n_n
	                	f1=nth_prime*ln_n
		                f2=ln_n_n-1i
		                n_f2=nth_prime*f2
		                boundlow=f1+n_f2
		                g1=nth_prime*ln_n_n
		                boundhigh=f1+g1
			else:
				boundlow=0
				boundhigh=4

                        diff=float(boundhigh-boundlow)
                        diff_low=n-boundlow
                        diff_high=boundhigh-n
                        diff_half=diff/2

			if nth_prime > 1 and nth_prime < 2010760:
				flag=True
				flag2=True
				if nth_prime >= 6:
					if n > boundhigh:
						flag=False
						counter_high+=1
					if n < boundlow:
						flag2=False
						counter_low+=1
				#print "'",nth_prime,"'th prime lowbound is:",boundlow,"<",n," <high bound:",boundhigh," diff:",diff," diff_low:",diff_low," diff_high:",diff_high," diff_half:",diff_half
			elif nth_prime >= 2010760:
				fraction=1/16597
				frac=1+fraction
				w=nth_prime*frac
				boundhigh=w
				print "'",nth_prime,"'th prime lowbound is:",boundlow,"<",n," <high bound:",boundhigh," diff:",diff," diff_low:",diff_low," diff_high:",diff_high," diff_half:",diff_half
			elif nth_prime==1:
				temp=0 #do nothing

		n+=1
	print "counter_high:",counter_high
	print "counter_low:",counter_low


if __name__ == '__main__':
	print "This program will generate a list of numbers starting at 2, and working up to the number you enter."
	print "It will list if it is a prime number or if it is not, and it will list the prime factorization"
	print ""
	print ""
	usernum=raw_input("What is the max number you would like to gernerate up to? ")
	usernum=int(usernum)
#	print Is_Prime.Is_Prime(usernum)
	print numlist(usernum)
