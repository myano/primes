#!/usr/local/bin/python

import Is_Prime

def findprimes(h):
    '''
    This function will generate a 'list' of prime numbers up to the given number inputted by the user.
    '''
    li=[]
        for n in range(2, h):
                j=0
        if Is_Prime.Is_Prime(n) == True:
            j+=1
            li.append(n)
    return li

if __name__ == '__main__':
    print getattr(findprimes,'__doc__')
    usernum=raw_input("Please enter up to what number you want to see a list of prime numbers: ")
    usernum=int(usernum)
    print findprimes(usernum)
