#!/usr/bin/python

import sys
import Is_Prime
import math

def genprime(p):
        '''Take incoming number 'p' and find the (p)th prime number'''
    j=1
    p=int(p)
    if p < 1:
        return False
    else:

        ln_n=(math.log(p))

        #print "ln_n:",ln_n

        ln_n_n=(math.log(ln_n))

        #print "ln_n_n", ln_n_n

        f1=p*ln_n
        f2=ln_n_n*p
        #n_f2=f2-p
        lowbound=f1+f2-p
        lowbound=math.floor(lowbound)
        lowbound=int(lowbound)
        g1=p*ln_n_n
        highbound=f1+g1
        highbound=math.floor(highbound)
        highbound=int(highbound)

        eachnum=2
        #highbound=int(p)**2
        nonprimes=0
        
        # I need to use the pi(x) function to find out how many primes come before the lowbound number
        
        print "lowbound: ",lowbound
        print "highbound: ", highbound
        while lowbound <= highbound:
            if Is_Prime.Is_Prime(lowbound)==True:
                print "value of p:",p
                #if j==p:
                print "eachnum:", eachnum
                print "lowbound:", lowbound
                return lowbound
                break
                print "j:", j
                #return lowbound
                j+=1
            else:
                nonprimes+=1
            #print "k:",k
            lowbound+=1
            
            
            #print "eachnum:",eachnum
            #eachnum+=1
            #j=float(j)
            #nonprimes=float(nonprimes)
            #total=nonprimes+j
            #percent_non=nonprimes/total*100
            #percent_j=j/total*100
        #print "\nnonprimes:",nonprimes, "  ",percent_non,"%"
        #print "primes:",j, "  ",percent_j,"%"


if __name__ == '__main__':
    usernum=raw_input("Please enter the (n)th prime number you want: ")
    usernum=int(usernum)
    print genprime(usernum)        
