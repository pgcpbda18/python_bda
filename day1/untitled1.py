#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:29:23 2026

@author: pgcp-esd


""" '''using if -else'''
'''a=int(input("enter the number a: "))
b=int(input("enter the number b: "))

if a > b:
    print(f"a is greater {a-b} by b")
else:
    print(f"b is greater {b-a} by a")
'''    
'''age=int(input("enter your age: "))
if age<=3:
    print("you are in kinder garden")
    print("you are not eligible to drive car")
    
elif age>3 or age<=5:
    print("you are in nursery school")
    
elif age<18:
    print("you are in high secondary school")
    
else:
    print("you are in college now")
'''
''' using for loop in python
for i in range(10):
    print(i,",",end=" ")
    
for i in range(2,10):
    print(i,",",end=" ")
 '''   
'''    
def addition(a,b):
    sum=a+b
    yield sum
'''
'using for loop to find prime number'
n=int(input("enter the number"))
for i in range(2,n):
    if n%i==0:
        print("it is not prime")
        break
else:
    print("it is a prime number")
    
