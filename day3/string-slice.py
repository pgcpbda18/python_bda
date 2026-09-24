#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:24:14 2026

@author: pgcp-esd
"""

'''
s="this is string"
print("length: ",len(s))
print("reverse: ",s[::-1])
print("even index: ",s[::2])
print("from 3 rd to 10th: ",s[3:11])
print("find values from the 5 till end: ",s[5:])
print("tp find the string from the beginning till 5th index: ",s[:6])
print("print frmom -9 and 11: ",s[-9:11]) 
''' 


s =" this is a cat, this is my cat, your cat is cute"
#print(w.rfind("cat")) 
'''
pos=s.find('cat')
while pos!=-1:
    print("pos: ",pos)
    pos=s.find('cat',pos+1)
 ''' 

pos=s.rfind("c")
while pos!=-1:
    print("pos: ",pos)
    pos=s.rfind()    