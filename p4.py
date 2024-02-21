# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:17:20 2023

@author: renuk
"""

##fizzbuzz problem

'''if any number is divisible by 3* print fizz 
 divisible by 5* then buzz
 15=  fizzbuzz 
'''
##by using for loop 
def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print('Buzz')
        else:
            print(i)
fizzbuzz(20)

## using dictionary
def fizzbuzz2(n):
    d={3:'Fizz',5:'Buzz'}
    for i in range(1,n+1):
        result=''
        for key,value in d.items():
            if i%key==0 :
                result+=value
        if not result:
            result=i
        print(result)
        
fizzbuzz2(20)






