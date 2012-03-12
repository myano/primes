#!/usr/local/bin/python

import sys
import Is_Prime
import generateprimes

listofprimefactors=[1]
def f(k,j):
        global listofprimefactors
        if k==0:
                print "k should be 0: ", k #through testing I have yet to have to happen, it is here just in-case       
        elif k==1:
                temp=0 #basically do nothing
        elif k==2:
                listofprimefactors.append(2)
        elif k==3:
                listofprimefactors.append(3)
        elif k % 2 == 0:
                listofprimefactors.append(2)
                f(k/2,j)
        elif k % generateprimes.genprime(j)==0:
                primenum=generateprimes.genprime(j)
                listofprimefactors.append(primenum)
                b=k/primenum
                j=1
                f(b,j+1)
        else:
                f(k,j+1)

	listofprimefactors=str(listofprimefactors)
        return listofprimefactors

if __name__ == '__main__':
	print "This program will provide the prime-factorization of a given number. It will then put the prime-factorization into a list and display it."
	print ""
	print ""
	usernum=raw_input("What number would you like the prime-factorization of? ")
        #usernum=1746860020068409
	usernum=int(usernum)
	qq=2
        print str(usernum) + " factorization is: " + str(f(usernum,qq))
