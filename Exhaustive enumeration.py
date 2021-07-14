#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:24:28 2021

@author: riya
"""

#Exhaustive enumeration


#Using while loop
cube = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(cube):
    ans += 1
    
if ans**3 != abs(cube):
    print(cube, "is not a perfect cube.")
else:
    if cube < 0:    
        print(str(-ans) + " is cube root of " + str(cube) + ".")
    else:
        print(str(ans) + " is cube root of " + str(cube) + ".")
        
        
        
#Using for loop       
#x = int(input("Enter an integer: "))
#for ans in range(abs(x) + 1):
#   if ans ** 3 == abs(x):
#        break
#if ans**3 != abs(x):
#   print(x, "is not a perfect cube.")
#else:
#   if x < 0:
#      ans = -ans
# print("Cube root of "+ str(x) + " is " + str(ans))