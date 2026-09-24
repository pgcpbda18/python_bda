#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:37:02 2026

@author: pgcp-esd
"""

import re


def is_phrase_palindrome(text):
    #clean the phrase by kepping only alphanumeric characters and converting to lower chase  
        cleaned_text = re.sub(r'^[0-9a-zA-Z]','',text).lower()
     #check the cleaned text is equal to phrase
        return cleaned_text == cleaned_text[::-1]
     

#test examples
phrases = ["Go hang a salami I'm a lasagna hog.","Was it a rat I saw?",
"Step on no pets","Sit on a potato pan, Otis","Lisa Bonet ate no basil",
"Satan, oscillate my metallic sonatas", "Hello, world!"]
         
         
for p in phrases:
    print(f"{p} ----->{is_phrase_palindrome(p)}")         
         
         