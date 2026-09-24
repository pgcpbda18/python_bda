#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:27:31 2026

@author: pgcp-esd
"""

from pythonstrings import *

print(lst)


x="hello"
y="hello"
print(id(x),id(y))
print(x is y)

y='welcome'
print(id(x),id(y))
print(x is y)

z=y
print(id(z),id(y))
print(z is y)

print(lst is lst2)


# the lst1 will automatically get the value of apppend item in the lst
# and you dont need to append the 100 in the lst1 becuase after intilization 
# the both lst are pointing to the same memory
lst1=lst
print(lst is lst1)
lst.append(100)
print(lst is lst1)


