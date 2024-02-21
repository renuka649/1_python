# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 19:21:07 2023

@author: renuk
"""

##prime number
##1 using flag
def prime(n):
    flag=0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
    if flag==0:
        print('prime')
    else:
        print('not prime')
n=int(input())
prime(n)

##2for else condition

def prime_number(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print('not prime')
                break
        else:
            print('yes, it is prime ')
    else:
        print('no')
s=int(input())
prime_number(s)







