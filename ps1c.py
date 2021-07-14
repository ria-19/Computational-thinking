#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:15:46 2021

@author: riya
"""

annual_salary = float(input("Enter your annual_salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
annual_return = 0.04
portion_down_payment = 0.25 * total_cost

low = 0
high = 10000
rate = (low + high) // 2

epilson = 100
numGuesses = 0
current_savings = 0

while abs(current_savings - portion_down_payment) >= epilson and (high - low) > 10:
    
    starting_salary = annual_salary
    months = 0
    current_savings = 0
    while months <= 36:
        current_savings += ((current_savings * annual_return) / 12) + ((starting_salary / 12) * (rate / 10000.0))
        months += 1
        if months % 6 == 0:
            starting_salary += (starting_salary * semi_annual_raise)
    
    if current_savings > portion_down_payment:
        high = rate
    else:
        low = rate
    rate = (high + low) // 2
    numGuesses += 1

if abs(current_savings - portion_down_payment) < epilson:
    print("Best saving rate: ", rate/10000.0)
    print("Steps in bisection: ", numGuesses)
else:
    print("It is not possible to pay the down payment in three years.")
    
    
            
    
    
    
        
    
    
    
        
    
    
  