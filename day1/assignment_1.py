#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:50:22 2026

@author: pgcp-esd
"""


def gcd(n,m):
    if n==0:
        return m
    if m==0:
        return n
    if(n>=m):
     return gcd(n-m,m)
    if(m>n):
     return gcd(m-n,n)
  

n=int(input("enter the number"))
m=int(input("enter the number"))
print(" ",gcd(n,m))

