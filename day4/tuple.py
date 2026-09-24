#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:56:00 2026

@author: pgcp-esd
"""
'''
a=1,2,3
a1=(3,"ccc",67)
x=a[0]
y=a[1]
z=a[2]

x,y,z=a
'''
def myf1(a=34,b=45,*t):
    
    print(a,b,t)
    s=a+b
    
    for num in t:
        s+=num
    return s

x=45
y=4
print(x,y)
p,q = myf1(x,y)

print(p,q)

lst=[1,2,3,410,23,23,12,23,2]

for num in sorted(lst):
    print(num)
    
for num in reversed(lst):
    print(num)
print(lst)

n=23
for idx,num in enumerate(lst):
    if num==n:
        print (idx,lst.count(n))

lst = ["pune","mumbai","delhi"]
#for idx,city in enumerate(lst,start=2):
 #   print(f"{idx} {city}")
    
lst1=[10,20,30,40]
for num, city in zip(lst1,lst):
    print(f"{num}----------{city}")