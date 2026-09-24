#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:23:21 2026

@author: pgcp-esd
"""

Notes = [2000,500,100,50,20,10,5,2,1]
Amount = int(input("Enter the amount: "))

for note in Notes:
    if Amount >= note:
        count_notes = Amount//note
        Amount = Amount%note
        label = "coin" if note in [1, 2, 5] else "note"
        print(f"{note} - {count_notes} {label}")