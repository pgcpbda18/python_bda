#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 02:11:48 2026

@author: pgcp-esd
"""

def longest_word(words,max_length):
    result = []    
    for word in words:
        if len(word) > max_length:
            result.append(word)
    return result

def main():
    word_list=['cdac','pune','mumbai','delhi']
    word_length = 4
    print(longest_word(word_list,word_length))
    
if __name__=="__main__":
    main()
