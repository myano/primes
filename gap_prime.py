#!/usr/local/bin/python

import math
import Is_Prime

def do_check(p):
    h=math.log(p)
#    print "here is h before being rounded: ", h
    h=int(round(abs(h)))
#    print "here is h rounded: ", h
    pminush=p-h
    pplush=p+h
    primes_nearby_true=False
    list_of_primes_nearby=[]
    while pminush <= pplush:
        check=Is_Prime.Is_Prime(pminush)
        if pminush!=p:
            if check==True:
                primes_nearby_true=True
                list_of_primes_nearby.append(pminush)
        pminush+=1
    if len(list_of_primes_nearby)==0:
        print pminush
        return False
    else:
        print pminush
        list_of_primes_nearby=str(list_of_primes_nearby)
        return list_of_primes_nearby

if __name__ == '__main__':
    again=True
    while again == True:    
        num=raw_input("What number do you want to test the 'Prime-counting function': ")
        num=int(num)
        print do_check(num)
        print "\n"
        goagain=raw_input("\nWould you like to try another number? (yes/no) ")
        if goagain == "yes" or goagain == "y":
            again=True
        else:
            again=False
        print "\n"
