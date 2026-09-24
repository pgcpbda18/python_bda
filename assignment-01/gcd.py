#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:40:56 2026

@author: pgcp-esd
"""

def find_gcd(a,b):
    while b != 0:
        a ,b = b, a%b
        
    return a

num1=int(input("enter first number to find GCD: "))
num2=int(input("enter second number: "))

gcd = find_gcd(num1, num2)

print(gcd)
