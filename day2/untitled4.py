#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:11:56 2026

@author: pgcp-esd
"""

num=int(input("enter the some choice"))
while(num!=7):
    num=int(input("your next choice"))
    match num:
     case 10:
      print(10)
     
     case 20:
        pass
    
     case 30:
        pass
     case _:
        print("enter a valid choice")
