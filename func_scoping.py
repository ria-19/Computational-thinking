#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:31:33 2021

@author: riya
"""
# def isIn(string_1, string_2):
#     if len(string_1) > len(string_2):
#         if string_2 in string_1:
#             return True
#         else:
#             return False
#     else:
#         if string_1 in string_2:
#             return True
#         else:
#             return False


# print(isIn('Priyanka', 'riya'))



# def printName(firstName, lastName, reverse):
#     if reverse:
#         print(lastName + ", " + firstName)
#     else:
#         print(firstName, lastName)
        
# printName('Lionel', 'Messi', True)
# printName('Lionel', 'Messi', reverse=False)


def f(x):
    y = 1
    x = x + y
    print('x = ', x)
    return x

x = 3
y = 2
z = f(x)
print('z = ', z)
print('x = ', x)
print('y = ', y)
