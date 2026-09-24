#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:17:16 2026

@author: pgcp-esd
"""

avg=0

print("enter 10 numbers")

for i in range(0,10):
    a=int(input(f"enter the {i+1}th number: "))
    avg=avg+a

avg=avg/10;

print(f"the average is {avg}")