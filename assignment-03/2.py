#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:29:30 2026

@author: pgcp-esd
"""

s1=input("enter a string : ")
s2=input("enter another string : ")

mid_index = len(s1)//2 

s1 = s1[:mid_index] + s2 + s1[mid_index:]
print(s1)