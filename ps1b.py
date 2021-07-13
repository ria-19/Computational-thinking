#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:14:05 2021

@author: riya
"""

annual_salary = float(input("Enter your annual_salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) 
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise: "))
portion_down_payment = 0.25 * total_cost
current_savings = 0
annual_return  = 0.04
months = 0

while current_savings <= portion_down_payment:
    months += 1
    current_savings += ((annual_return * current_savings) / 12) + portion_saved * (annual_salary / 12)
    
    if months % 6 == 0:
        annual_salary += (semi_annual_raise * annual_salary)
    
    
print("Number of months:", months)