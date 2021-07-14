#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:24:29 2021

@author: riya
"""

x = 0.009
epilson = 0.01
numGuesses = 0
low = 0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= epilson:
    print("low = ", low, "high= ", high, "ans =", ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/ 2.0
print("numGuesses: ", numGuesses) 
print(ans, "is close to squre root of", x)