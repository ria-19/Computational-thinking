#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:16:08 2021

@author: riya
"""

# Using Newton-Raphson Method to find solution of polynomial with one variable
#x**2 - 24 = 0
# 2x
# guess - p(guess)/p'(guess)

epilson = 0.01
y = 625.0
guess = y/2.0
numGuess = 0

while abs(guess*guess - y) >= epilson:
    numGuess += 1
    guess = guess - (((guess**2) - y)/(2 * guess))
    
print("Squre root of", y, 'is about', guess)
print("NumGuesses: ", numGuess)
    
    
    