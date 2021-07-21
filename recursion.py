#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:16:09 2021

@author: riya
"""

# def isPalindrome(s):
#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 ans = ans + c
#         return ans
    
    
#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1: -1])
        
        
#     return isPal(toChars(s))


# print(isPalindrome('Able was I, ere I saw Elba'))


def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))



def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
        
        
