#!/usr/bin/python

import sys
import math
import Is_Prime
import generateprimes

def show_diff(n):
    p=1
    num_trues=0
    num_falses=0
    #e=2.71828182845904523536
    f=1.5
    while p <= n:
        num=generateprimes.genprime(p)
        num1=generateprimes.genprime(p+1)
        #num_log=math.log(num)
        #num_log=int(abs(num_log))
        num1_log=(math.log(num1))**f
        num1_log=int(round(num1_log))
        diff=num1-num
        isit=False
        #num1_log_p=num1/num1_log
        if diff <= num1_log:
            isit=True
            num_trues+=1
        else:
            isit=False
            num_falses+=1
        print num1, "-", num, "=", diff, "-is diff <= log(", num1, ")", "...", isit, "      range: ", num1_log
        p+=1
    num_falses=float(num_falses)
    num_trues=float(num_trues)
    total=num_falses+num_trues
    percent_true=num_trues/total*100
    percent_false=num_falses/total*100
    print "Total 'True's: ", num_trues, "   ", percent_true,"%"
    print "Total 'False's: ", num_falses, "   ", percent_false,"%"

if __name__ == '__main__':
    usernum=raw_input("Please enter the highest 'n'th prime number you would like to show the differences between: ")
    usernum=int(usernum)
    show_diff(usernum)
