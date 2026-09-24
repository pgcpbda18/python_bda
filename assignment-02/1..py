#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:11:17 2026

@author: pgcp-esd
"""

Total_lectures = int(input("enter the total number of lectures held : "))
Attended_lectures =int(input("enter the number of lectures attended : "))

Attendance = (Attended_lectures/Total_lectures)*100
print("Your Attendance is : ",Attendance)
if Attendance > 75 :
    print("You are eligible for exam")
else:
    medical_input=input("If you have a medical cause enter (Y/N) :").strip().upper()
    if medical_input == 'Y' and Attendance > 50:
        print("You can give the exam")
    else:
     print("You are not eligible for exam")

    
