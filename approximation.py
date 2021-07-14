#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:51:16 2021

@author: riya
"""

x = 123456
epilson = 0.01
step = epilson ** 2
numGuess = 0
ans = 0.0
while abs(ans**2 - x) >= epilson and ans*ans <= x:
    ans += step
    numGuess += 1

print("numGuesses: ", numGuess)
if abs(ans**2 - x) >= epilson:
    print("Failed on square root of", x)
else:
    print(ans, "is close to squre root of", x)