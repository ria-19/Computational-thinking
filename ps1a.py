#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:27:47 2021

@author: riya
"""

annual_salary = float(input("Enter your annual_salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) * (annual_salary / 12)
total_cost = float(input("Enter the cost of your dream house: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
annual_return  = 0.04
months = 0

while current_savings <= portion_down_payment:
    current_savings += ((annual_return * current_savings) / 12) + portion_saved
    months += 1
    
print("Number of months:", months)