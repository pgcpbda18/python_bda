#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:49:22 2026

@author: pgcp-esd
"""

num=int(input("enter a number : "))

count=0
sum=0

while num>0:
    count = count + 1
    d=num%10
    num=num//10
    sum=sum+d
    
print(f"number of digits is is {count}")
print(f"sum of digits is {sum}")