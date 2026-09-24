#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:18:42 2026

@author: pgcp-esd
"""

Units_consumed=int(input("Enter the units consumed : "))
 
if Units_consumed <100:
    print("NO BILL")
elif Units_consumed < 200:
    bill=(Units_consumed -100)*5
    print(bill)
elif Units_consumed > 200:
    bill= (Units_consumed-200)*10 +500
    print(bill)