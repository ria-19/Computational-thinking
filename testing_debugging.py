#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:09:36 2021
#6.0001 class examples
@author: riya
"""

# Handlers for exceptions in python


# Without try&except
# a = int(input("Tell me one number: "))
# b = int(input("Tell me another number: "))
# print(a/b)
# print("I will run only if above lines are okay")


#With try&except
# try:
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print(a/b)
# except:
#     print("Bug in user input.")
    
# print('I will still run in this case.')

# Handling specific exceptions
# try:
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print("a/b =", a/b)
#     print("a+b =", a + b)
# except ValueError:
#     print("Could not convert to a number.")
# except ZeroDivisionError:
#     print("Can't divide by zero.")
# except:
#     print("Something went very wrong.")
# print("Anyways moving on.")
    


#other exceptions
# try:
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print(a/b)
# except ValueError:
#     print("Could not convert to a number.")
# except ZeroDivisionError:
#     print("Can't divide by zero.")
# except:
#     print("Something went very wrong.")
# else:
#     print("Yeah!! No error.")
# finally:
#     print("I will run no matter what!")
# print("if there are errors")
    

#Raising an exception
# def get_ratios(L1, L2):
#     """Assumes: L1 and L2 are lists of equal length of numbers
#     Returns: a list containing L1[i]/L2[i]"""
    
#     ratios = []
#     for index in range(len(L1)):
#         try: 
#             ratios.append(L1[index]/L2[index])
#         except ZeroDivisionError:
#             ratios.append(float('nan'))
#         except:
#             raise ValueError('get_ratios called with bad args')
#     return ratios

# L1 = [1, 2, 3, 4, 0, 0]
# L2 = [2, 4, 6, 8]
# print(get_ratios(L1, L2))


#Examples of Exceptions
test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], [['bruce', 'wayne'],[100.0, 80.0, 74.0]], [['captain', 'america'], []]]


# def get_stats(class_list):
#     new_stats = []
#     for elt in class_list:
#         new_stats.append(elt[0], elt[1], avg(elt[1]))
#     return new_stats

# # Without try and except
# def avg(grades):
#     return sum(grades)/len(grades)

# # With try and except
# def avg_withtry(grades):
#     """If list is empty, it will return a 0"""
#     try:
#         return sum(grades)/len(grades)
#     except:
#         print('warning: no grades data')
#         return 0.


# Assertions
def avg_with_assert(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/ len(grades)
avg_with_assert([]j)
    
    
        





