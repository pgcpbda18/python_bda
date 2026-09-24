#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:08:33 2026

@author: pgcp-esd
"""

import math

x = float(input("Input the value of x : "))
n = int(input("Input number of terms : "))
    
total_sum = 0

for i in range(n):
    term = (x ** i) / math.factorial(i)
    total_sum += term
        
print(f"The sum is : {total_sum:.6f}")

