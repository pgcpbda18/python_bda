#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:53:21 2026

@author: pgcp-esd
"""
#list in python
lst=[12,'xxx',2,3,[10,2]]
lst2=[12,13,14,10,4,5,23,12,13]

for num in lst:
    print(num,end=" ")
 
#add at the end
lst.append(49)
lst.append('xxxx')
print(lst)

print()
#add multiple items in the list in the end of the list
lst.extend([1,2,3,4,565,5,6,6])
lst.extend("avengers")
print(lst)

#Insert function to input any value in the list at any index
print()
lst.insert(1, "endgame")
print(lst)


#shows the index of particular list element 
print(lst.index("endgame"))

#delete data from the list
lst.pop(1)
print(lst)


if 'xxx' in lst:
    print("yeh idar hae")
else:
    print("yeh idar nahi hae")
    
#overwriting values in the list using index of the list
lst[3]=45

