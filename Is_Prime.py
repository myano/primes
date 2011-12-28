#!/usr/bin/python

import math

def Is_Prime(p):
    '''
    This function determines if a given number 'p' is a prime number or not.
    '''
    p = int(abs(p))
    x = math.floor(math.sqrt(p))
    a = 3
    #z=x
    if p == 0:
        return False
    elif p == 1:
        return False
    elif p == 2:
        return True
    elif p % 2 == 0:
        return False
    elif p >= 9:
        if x % 2 == 0:
            x += 1
        while x >= 3:
            if p % x == 0 or p % a == 0: return False
            x -= 2
            a += 2
    return True

if __name__ == '__main__':
    #print getattr(Is_Prime,'__doc__')
    #num=raw_input("What number do you want to test? (To see if it is a prime?): ")
    num=1746860020068409
    #num=982451653
    num=int(num)
    if Is_Prime(num) == True:
        print "The number, ", num, " is a prime number!"
    else:
        print "The number, ", num, " is a composite number!"
