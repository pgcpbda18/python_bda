#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:46:20 2026

@author: pgcp-esd
"""

count = 0
total_sum = 0
product = 1

while True:
    user_input = input("Enter an integer (or press 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break  
    else:
        num = int(user_input)
        count += 1
        total_sum += num
        product *= num



if count > 0:
    average = total_sum / count

    print(f"Average: {average}")
    print(f"Product: {product}")
