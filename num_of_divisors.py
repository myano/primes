#!/usr/bin/python

import sys
import math

def find(j):
    ''' This functions takes an incoming value 'j' and calculates the numberof divisors j has. '''
    s=2
    value=0
    while s <= math.floor(math.sqrt(j)):
        value+=((math.floor(j/s))-(math.floor((j-1)/s)))
        s+=1
    return value

if __name__ == '__main__':
    print "Please input a number you would like to the know the amount of divisors it has.\n"
    usernum=raw_input("Please enter a number: ")
    #usernum=982451653
    #usernum=1425172824437699411
    #usernum=119218851371
    usernum=int(usernum)
    print find(usernum)
