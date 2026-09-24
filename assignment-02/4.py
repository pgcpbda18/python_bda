#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:08:02 2026

@author: pgcp-esd
"""

# Ask the user to enter their marks
marks = float(input("Enter your marks: "))

# Check the range and print the grade
if marks < 25:
    print("Grade: F")
elif 25 <= marks < 45:
    print("Grade: E")
elif 45 <= marks < 50:
    print("Grade: D")
elif 50 <= marks < 60:
    print("Grade: C")
elif 60 <= marks < 80:
    print("Grade: B")
else:
    print("Grade: A")
