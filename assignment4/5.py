#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 00:53:10 2026

@author: pgcp-esd
"""
def recursive_sum(n):
    """Calculates the sum from 1 to n recursively"""
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

def main():
    """Calls the recursive sum function"""
    print(recursive_sum(10))

if __name__ == "__main__":
    main()




