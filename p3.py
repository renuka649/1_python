# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:50:54 2023

@author: renuk
"""

#3 compress string
#input='aabbccaaafffgggghhhiii'
#output='a2b2c2a3f3g4h3i3'

#by using for loop
def compress(s):
    n=len(s)
    new_s=''
    count=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            new_s+=(s[i]+str(count))
            count=1
    new_s+=(s[n-1]+str(count))
    return new_s
s=input()
print(compress(s))

#using while loop
def compress2(s):
    n=len(s)
    new_s=''
    i=0
    while(i<n-1):
        count=1
        while(i<n-1 and s[i]==s[i+1]):
            count+=1
            i+=1
        i+=1
        new_s+=(s[i-1]+str(count))
    return new_s


s=input()
print(compress2(s))










