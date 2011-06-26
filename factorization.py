#!/usr/local/bin/python

import generateprimes

listofprimefactors=[]
def f(k,j):
        '''
	This function 'f' takes a give number 'k' and produces the Prime-Factorization in the form of a list, excluding the number one and the given number.

	'j' here is a counter for the 'j'th prime number.

	If you would like this in a pretty print format I have made a for loop inside "numlist_prime.py" which turns the list into "a * b * c" etc.. 
	'''
	global listofprimefactors
        if k==0:
		temp=0
		print temp #I've never encountered this, but just in case ;)
	elif k==1:
		temp=0 #basically do nothing, this still has to be here so it doesn't do the "else" statement an extra time
        elif k==2:
                listofprimefactors.append(2) #Adds 2 as a factor if k is equal 2
        elif k==3:
                listofprimefactors.append(3) #Adds 3 as a factor if k is equal to 3
        elif k % 2 == 0:
		#If divisble by add 2 as a factor to k
                listofprimefactors.append(2)
                f(k/2,j) #call to recursion, but the new value of k is half of k, because we havae just accounted for k being divisble by 2
        elif k % generateprimes.genprime(j)==0:
		#This is a bit copmlicated, but basically what this does is: if the value of k is evenly divisble by the 'j'th prime number then add that 'j'th prime nubmer as a factor. The first time this elif statement runs the "generateprimes.genprime(j)" will equal 3
                primenum=generateprimes.genprime(j)
                listofprimefactors.append(primenum)
                b=k/primenum #since we have just accounted for the "prime factor" we need to move on, so we divide k by that prime number and send that new value of k (b) to the call of recursion
                j=1 #j is always set to 1 here because the first time a number (k) is divisble by a prime number, the next time it goes to the call of recursion the value of j will be 2. 
                f(b,j+1) #j will be equal to 2, the first time this elif statement runs through. 
        else:
                f(k,j+1) #if k was not divisble by anthing above, increase the value of j. This allows the 'j'th prime number to increase by one. So the first time this runs if k is not divisble by the (j=2) 2nd prime number (which is 3), then increase j to 3 (j=3). This way the second time through it will check to see if k is evenly divisble by the 3rd prime number (which is 5). and so on...

	return listofprimefactors

if __name__ == '__main__':
	usernum=raw_input("What number would you like the prime-factorization of? ")
	#usernum=1746860020068408
	usernum=int(usernum)
	qq=2
	print f(usernum,qq)
