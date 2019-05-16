#!/usr/bin/python

import sys
import math
import generateprimes

def show_diff(n):
    ''' This function goes from the first prime (2), up to the 'n'th prime number you specify and tests to see if result of the following function given that prime is greater than or equal to the difference of the two prime number mentioned. The forumla: num1_log=(math.log(num1))**my_constant_a. Where num1 is the 'p'th prime number. And 'my_contant_a' is 1.72 (subject to change)'''
    p=1
    num_trues=0
    num_falses=0
    #e=2.71828182845904523536 # ... 100% but bounds are too far apart!
    #f=1.5 # only yields...
    #phi=1.61803398874989484820458 # yields 99+% for first 150 primes
    #super_phi=e/phi # yeilds only only 'False' in the first 1000 primes
    #my_constant=1.70 # yields only only 'False' in the first 1000 primes
    my_constant_a=1.78107241799019798523650410
    print "Value of 'my_constant_a': ", my_constant_a
    while p <= n:
        num=generateprimes.genprime(p)
        num1=generateprimes.genprime(p+1)
        #num_log=math.log(num)
        #num_log=int(abs(num_log))
        num1_log=(math.log(num1))**my_constant_a
        num1_log=int(math.ceil(num1_log))
        diff=num1-num
        isit=False
        #num1_log_p=num1/num1_log
        if diff <= num1_log:
            isit=True
            num_trues+=1
        else:
            isit=False
            num_falses+=1
            print num1, "-", num, "=", diff, "-is diff <= log(", num1, ")^1.7810724", "...", isit, "      range: ", num1_log
        p+=1
    num_falses=float(num_falses)
    num_trues=float(num_trues)
    total=num_falses+num_trues
    percent_true=num_trues/total*100
    percent_false=num_falses/total*100
    print "Total 'True's: ", num_trues, "   ", percent_true,"%"
    print "Total 'False's: ", num_falses, "   ", percent_false,"%"

if __name__ == '__main__':
    print "\Calculating the difference between primes up to the 'n'th prime number specified. Also testing the formula: num1_log=(math.log(num1))**my_constant_a. Where num1 is the 'p+1'th prime number and p is the previous prime number."
    print "\nThis program checks to see if the difference between each prime number is <= the num1_log."
    usernum=raw_input("\nPlease enter the highest 'n'th prime number you would like to show the differences between: ")
    usernum=int(usernum)
    show_diff(usernum)
