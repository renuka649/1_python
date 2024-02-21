# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:27:16 2023

@author: renuk
"""

#1#palindrome string
s =input()
temp=s[::-1]
if s==temp:
    print('it is pallindrome string....')
    print(s)

else:
    print('not a pallindrome....')
#or   
#using for loop
def pallindrome(s):
    n=len(s)
    for i in range(n):
        if s[i]!=s[n-i-1]:
            return False
        else:
            return True
s=input()
pallindrome(s)            

#or
#by using reverse and join inbuilt function
def pallindrome(s):
    temp=''.join(reversed(s))
    print(temp)
    if s==temp:
        return True
    else:
        return False
s=input()
pallindrome(s)  

#or 
# by using while loop
def pallindrome(s):
    n=len(s)
    f=0
    l=n-1
    while(f<l):
        if s[f]==s[l]:
            f+=1
            l-=1
        else:
            return False
    return True
s=input()
pallindrome(s)            

#palindrome number
#not good way
s =int(input())
s=str(s)
temp=s[::-1]
if s==temp:
    print('it is pallindrome string....')
else:
   print('not a pallindrome....')
   
#or 
#by using while loop 
def pallindrome(n):
    temp=n
    rev=0
    while(temp>0):
        d=temp%10
        rev=d+rev*10
        temp=temp//10
    if n==rev:
        print('pallindrome')
    else:
        print('not pallindrome...')
pallindrome(123)   
    