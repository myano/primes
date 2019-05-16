#!/usr/local/bin/python

import sys
import Is_Prime
import math

def numlist(h):
    #listofprimefactors=[]
    list_primes=[]
    #for n in range(2, h+2):
    n=2
    line=0
    while n <= (h):
        if Is_Prime.Is_Prime(n)==True: #if prime originally was "elif: x == n-1:"
            list_primes.append(n)
        n+=1
    print "'",len(list_primes),"'th prime number:",list_primes[-1]
    guess_b4=(math.log(h)-math.log(2))
    print "ln(",h,") - ln(2): ",guess_b4

if __name__ == '__main__':
    print "This program will display the nearest prime number below the inputted number."
    print "It will also provide it's position, for example if you enter 10. It will display '4'th prime number is: 7"
    print "Because the nearest prime number under 10 is 7, and 7 is the 4th prime number."
    print ""
    print ""
    usernum=raw_input("What is the max number you would like to gernerate up to? ")
    usernum=int(usernum)
#    print Is_Prime.Is_Prime(usernum)
    print numlist(usernum)
