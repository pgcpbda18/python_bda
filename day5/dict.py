#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:42:48 2026

@author: pgcp-esd
"""

from set import *
d1['a']=100
v=d1.get('a',-1)

if v!=-1:
    d1['a']=300
else:
    print("key exists")
    
v=d1.setdefault('a',567)
lst=['pune','mumbai','delhi']
d3=dict.fromkeys(lst,100)

#delete the last key ,value pair
d1.popitem()

#to delete Given key, value pair
d1.pop('a',-1)

c={'java':100,"python":200,"linux":150}
#find all courses with capacity 100

'''for k in c.keys():
    print(f"{k}----->{c[k]}")
'''    
for k,v in c.items():
    print(f"{k}---->{v}")
    
import re
s="hi my name is Bruce"
obj = re.search(".*bruc.*", s , re.I|re.M)

if obj!=None:
    print(obj.group())
    print(obj.span())
    
