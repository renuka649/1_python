# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:49:29 2023

@author: renuk
"""

####Character occurence
#1. least repeating character in a string
 ##using dictionary
def least_char_occurence(s):
    ch={}
    for i in s:
        if i in ch:
           ch[i]=ch[i]+1
        else:
            ch[i]=1

    print(ch)
    result=min(ch,key=ch.get)
    print(result)
s='fhhhhhhhjjggdeynndawfvmkufre'
least_char_occurence(s)    
 


##using in-built function counter
from collections import Counter
s='sgddffffhsdrybvnbnvgvvbcgjmdfc'
result=Counter(s)
result
result=min(result,key=result.get)
result


#2. Count of any perticluar element

#by using count function
s='rreufihasodhudfncsildocvapm'
print(s.count('r'))

#using dict
def count_char_occurence(s,search):
    ch={}
    for i in s:
        if i in ch:
           ch[i]=ch[i]+1
        else:
            ch[i]=1
    try:
        print(ch[search])
    except:
        print(0)
s='fhhhhhhhjjggdeynndawfvmkufre'
count_char_occurence(s,'z')  


#3. Count of all elements


def all_char_occurence(s):
    ch={}
    for i in s:
        if i in ch:
           ch[i]=ch[i]+1
        else:
            ch[i]=1

    print(ch)


s='fhhhhhhhjjggdeynndawfvmkufre'
all_char_occurence(s) 



