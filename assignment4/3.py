#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:06:53 2026

@author: pgcp-esd
"""



def is_panagram(sentence):
    # ADD THE SENTENCE IN THE SET
    char_set = set(sentence.lower())
    
    alpha_set = set("qwertyuiopasdfghjklzxcvbnm")
    
    return alpha_set.issubset(char_set)

test_sentence=["The quick brown fox, jumps over the lazy dog!!!!",
    "Hello, world!"]

for p in test_sentence:
    print(f"{p} ----> {is_panagram(p)}")

