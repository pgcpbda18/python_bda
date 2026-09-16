#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:18:03 2026

@author: pgcp-esd
"""

class calculator:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
class method(calculator):
    def print_result(self):
       print("", self.add(4,5))

obj=method()
obj.print_result()
        