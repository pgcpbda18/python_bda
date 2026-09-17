#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:14:42 2026

@author: pgcp-esd
"""


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
    
n=int(input("enter your number: "))
print("Factorial of the given number is ", factorial(n))
print("Addition of the given number is ",sum(n))


