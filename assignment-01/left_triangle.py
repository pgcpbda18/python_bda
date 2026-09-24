#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:24:04 2026

@author: pgcp-esd
"""

n=int(input("enter a number : "))

for i in range(1, n):
    print("*" * i)
    
    
    
    
for i in range(1, n, 2):
    print("*" * i)
for i in range(n//2, 0, -2):
    print("*" * i)
    
    
for i in range(n, 0, -1):
    for j in range(2 * i - 1):
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()
    
    
    
for i in range(1, n):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()