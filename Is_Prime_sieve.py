#!/usr/bin/python

import math

def Create_Sieve(n):
    k=2
    sieve_list=[]
    while k <= math.floor(math.sqrt(n)):
        sieve_list.append(k)
        k+=1
    #print sieve_list
    c=0
    m=0
    while c < len(sieve_list):
        k=sieve_list[c]
        #print "value of k:",k
        m=c+1
        #print "m, before m-while look:", m
        if sieve_list[c]**2 < sieve_list[-1]:
            if n % sieve_list[m] == 0:
                return False
            while m < len(sieve_list):
                #m=c
                #print "value of sieve_list[m]:",sieve_list[m]
                if sieve_list[m] % k == 0:
                    del sieve_list[m]
                m+=1
        else:
            break
        c+=1
    #return sieve_list
    print "Generated Sieve_List"
    v=0
    while v < len(sieve_list):
        if n % sieve_list[v] == 0:
            return False
        v+=1
    return True    
        

def Is_Prime(k):
    ''' This function determines if a given number 'p' is a prime number or not. '''

        
        
            
if __name__ == '__main__':
    num=raw_input("What number do you want to test? (To see if it is a prime?): ")
    #num=1746860020068409
    #num=13091204281
    #num=982451653
    #num=119218851371
    num=int(num)
    #print Is_Prime(num)
    #new_list=Create_Sieve(num)
    #print new_list
    #print "Size of list:",len(new_list)
    if Create_Sieve(num) == True:
        print "\nThe number, ", num, " is a prime number!"
    else:    
        print "\nThe number, ", num, " is a composite number!"
