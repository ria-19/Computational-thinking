#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:12:04 2021

@author: riya
"""



class Coordinate(object):
    """
    A representation of a coordinate point
    """
    def __init__(self, x, y):
        """ x and y are integers"""
        self.x = x
        self.y = y
    
    def distance(self, other):
        """ distance between x and y """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
    def __str__(self):
        """ what prints if print() is called on coordinate object"""
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    def __add__(self, other):
        """ add x to x and y to y of both object"""
        return (self.x + other.x, self.y + other.y)
     
    def __sub__(self, other):
        """ subtract x of object on which it is called from x and y from y """
        return (self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """ checks if they lie in same point"""
        return self.x == other.x and self.y  == other.y
    
        
c1 = Coordinate(3, 4)
origin = Coordinate(0, 0)
distance = c1.distance(origin) #Coordinate.distance(c, zero)
c2 = Coordinate(-2, 5)
print(c1 + c2)
print(c1 - c2)
print(c1 == c2)



class Fraction(object):
    """ num and denom are integers"""
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
        
    def __str__(self):
        """ Returns strings represention of fraction"""
        return str(self.num) + "/" + str(self.denom)
    
    def __add__(self, other):
        """Returns a new fraction representing the sum of passed two fraction object"""
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """Returns a new fraction representing the substraction of passed two fraction object"""
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """Returns a float value of the fraction"""
        return self.num/self.denom
    def inverse(self):
        """Returns a new fraction representing inverse of the passed fraction"""
        return Fraction(self.denom, self.num)


a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b 
print(c)
print(float(c))
print(Fraction.__float__(c))
print(type(c))
print(a.inverse())


    
    
    
    
    
        
