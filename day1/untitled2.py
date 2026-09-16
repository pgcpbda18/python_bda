#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:11:20 2026

@author: pgcp-esd
"""

num=2345
s=0
while num>0:
    d=num%10
    s+=d
    num=num//10
print("addition of digits:",s)