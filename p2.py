# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:27:28 2023

@author: renuk
"""

#2 fibonacci series
#0,1,1,2,3,5,8,13,......

#by using while loop
def fibonacci(n):
    f=0
    s=1
    print(f)
    while(s<n):
        print(s)
        Next=f+s
        f=s
        s=Next
n=int(input())
fibonacci(n)

#or
n=int(input())
f=0
s=1
print(f)
while(s<=n):
    print(s)
    f,s=s,f+s
print(f)

#by using for loop
#it will print given number of values not upto that given values
def fibonacci1(n):
    f,s=0,1
    if n==1:
        print(f)
    else:
        print(f)
        print(s)
        for i in range(2,n):
            c=f+s
            f=s
            s=c
            print(c)
n=int(input())
fibonacci1(n)

#or
#recursion
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=10
if n<=0:
    print('invalid')
else:
    for i in range(n):
        print(fib(i))
        
        
        