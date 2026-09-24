#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:26:18 2026

@author: pgcp-esd
"""
# Ask the user to enter the cost price of the bike
cost_price = float(input("Enter the cost price of the bike (in Rs): "))

# Calculate tax and insurance percentages based on the criteria
if cost_price > 100000:
    tax_percent = 15
    insurance_percent = 20
elif 50000 < cost_price <= 100000:
    tax_percent = 10
    insurance_percent = 8
else:
    tax_percent = 5
    insurance_percent = 5

# Calculate final amounts
road_tax = (tax_percent / 100) * cost_price
insurance = (insurance_percent / 100) * cost_price
total_amount = cost_price + road_tax + insurance

# Display the breakout amounts
print("\n--- Price Breakdown ---")
print(f"Cost Price: Rs {cost_price:,.2f}")
print(f"Road Tax ({tax_percent}%): Rs {road_tax:,.2f}")
print(f"Insurance ({insurance_percent}%): Rs {insurance:,.2f}")
print("-----------------------")
print(f"Total Amount to Paid: Rs {total_amount:,.2f}")
