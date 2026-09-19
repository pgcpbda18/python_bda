#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:03:08 2026

@author: pgcp-esd
"""
def f1(x=10):
    ''' This is about f1 : prints the parameter'''
    print("inside function 1",x)
    
def f2():
    print("inside fucntion 2")
 

if __name__=="__main__":
    
   f1(100)
   f1()
   f2()
   