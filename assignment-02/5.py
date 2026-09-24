#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:09:53 2026

@author: pgcp-esd
"""

number=int(input("Enter the number:"))
if number%5==0 and number%11==0:
    print("It is divisible by 5 and 11")
elif number%5==0:
    print("It is divisible by 5")
elif number%11==0:
    print("It is divisible by 11")
else:
    print("It is not divisible by 5 and 11")
    
    
    