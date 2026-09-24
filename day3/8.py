#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:05:31 2026

@author: pgcp-esd
"""


n = int(input("Enter the number of terms: "))
    
if n <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    total_sum = 0
    current_term = 9
    series = []
        
    for _ in range(n):
        series.append(str(current_term))
        total_sum += current_term
        current_term = current_term * 10 + 9
     
    print(f"Series: {' + '.join(series)}")
    print(f"Sum of the series: {total_sum}")

