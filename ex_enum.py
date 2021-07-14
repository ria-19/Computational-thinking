#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:52:39 2021

@author: riya
"""


num = int(input("Enter an integer: "))
pwr = 1

while pwr < 6:
    root = 0
    while root**pwr < num:
        root += 1
    if root**pwr != num:
        print("Couldn't find perfect integer pair.")
    else:
        print("root: ", root, "pwr: ", pwr)
    pwr += 1

    

    

