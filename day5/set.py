#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:28:20 2026

@author: pgcp-esd
"""

S=set()
d=dict()
print(type(d))
print(type(S))

s={"python","perl","Python","python","java"}
print(s)

str="pgcpbdapgcpbda"

s1 = set(str)
print(s1)
print(len(s1))

s1.update([23,46,78,89])
print(s1)

s.add(23)
print(s)
if 23 in s:
    s.remove(23)
print(s)
s1={1,2,3,4,5}
s2={4,5,11,12}
print("Intersecion",s1.intersection(s2),s1&s2)
print(s1)
print("union",s1.union(s2),s1|s2)
print("difference",s1.difference(s2),s1-s2)
print("symmetric difference",s1.symmetric_difference(s2),s1^s2)
d1={'a':100,'b':234,'c':200}
d2={"x":20,'y':23,'z':345}
d1.update(d2)
print(d1)
d3={**d1,**d2}
print(d3)
d1['d']=56
print(d1)