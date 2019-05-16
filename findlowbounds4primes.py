#!/usr/bin/python

import sys
import generateprimes

def newfunc(m):
    m=int(m)
    for eachnum in range(2, m):
        k=3/2
        compareme=(eachnum**k)
        print "here is the 'compare-me' to the power of 3/2: ", compareme
        comparemeagain=compareme/2
        comparemeagain=int(comparemeagain)
        generatedprime=generateprimes.genprime(eachnum)
        if comparemeagain < generatedprime:
            print eachnum, " is TRUE for this case. Here is the prime ", generatedprime, "here is the 'compare-me': ", comparemeagain
        else:
            print eachnum, " is FALSE."
        eachnum+=1
    
if __name__ == '__main__':
    usernum=raw_input("Please enter the times n, number you would like to find the lower bound... hehe ")
    print newfunc(usernum)
