#!/usr/bin/python

import Is_Prime

def genprime(p):
        '''Take incoming number 'p' and find the (p)th prime number'''
        j=1
        j=int(j) #makes sure j is of type Integer and not a string
    highestvalue=300000000
        for eachnum in range(2, highestvalue):
                if Is_Prime.Is_Prime(eachnum)==True:
                        if j==p:
                                return eachnum
                                break
            j+=1

if __name__ == '__main__':
    usernum=raw_input("Please enter the (n)th prime number you want: ")
    usernum=int(usernum)
    print genprime(usernum)    
