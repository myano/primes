#!/usr/local/bin/python

import Is_Prime
import generateprimes
import factorization

def numlist(h):
    '''
    This program will generate a list of numbers starting at 2, and working up to the number you enter. 

    It will list if it is a prime number of it is not, and it will list the prime factorization.
    '''
    listofprimefactors=[]
    for n in range(2, h+1):
        if Is_Prime.Is_Prime(n)==True:
            print n, 'is a prime number'
        elif Is_Prime.Is_Prime(n)==False:
            i=0
            del listofprimefactors[:]
            del factorization.listofprimefactors[:]
            incomingfactors=factorization.f(n,2)
            listofprimefactors.extend((incomingfactors))
            prettyprintstring=""
            for eachfactor in listofprimefactors:
                eachfactor=str(eachfactor)
                prettyprintstring+=eachfactor
                if len(listofprimefactors)-1 > i:
                    prettyprintstring+=' * '
                    i+=1
            print n, 'is ', prettyprintstring
    return ""

if __name__ == '__main__':
    print getattr(numlist,'__doc__')
    usernum=raw_input("What is the max number you would like to gernerate up to? ")
    usernum=int(usernum)
    #print "Is_Prime.Is_Prime(usernum): ", Is_Prime.Is_Prime(usernum)
    print numlist(usernum)
