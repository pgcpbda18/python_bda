#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:43:45 2026

@author: pgcp-esd
"""

def translate(text):
    consonants ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result=[]
    
    for char in text:
        if char in consonants:
            middle_o = 'O' if char.isupper() else 'o'
            result.append(char+middle_o+char)
        else:
            result.append(char)
            
    return "".join(result)

print(translate("this is fun"))
            