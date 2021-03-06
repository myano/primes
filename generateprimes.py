#!/usr/bin/env python

import Is_Prime
import math

def genprime(p):
        '''Take incoming number 'p' and find the (p)th prime number'''
        j=1
        p=int(p) #makes sure j is of type Integer and not a string
    highbound=0

    if p <= 9:
        highbound=100
    else:
        #calculate a reasonable "higestvalue"
        ln_n=(math.log(p))
        ln_n_n=(math.log(ln_n))

        f1=p*ln_n
        g1=p*ln_n_n
        highbound=f1+g1
        highbound=math.floor(highbound)
        highbound=int(highbound)
        #print "highbound:", highbound

    # find the nth prime number...
        if p >= 5:
            m = p
        else:
            m = 2
        for eachnum in range(m, highbound):
                if Is_Prime.Is_Prime(eachnum)==True:
                        if j==p:
                                return eachnum
                                break
            #print "j:",j
            j+=1

if __name__ == '__main__':
    #usernum=raw_input("Please enter the (n)th prime number you want: ")
        usernum = 34783
    usernum=int(usernum)
    print genprime(usernum)    
