#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:59:08 2026

@author: pgcp-esd
"""

even_sum = 0

print("enter 20 numbers:")
for i in range(1, 21):
    while True:
        num = int(input(f"Enter number {i}: "))     
        if num % 2 == 0:
            even_sum += num     
        break
            

print(f"\nThe sum of all even numbers entered is: {even_sum}")