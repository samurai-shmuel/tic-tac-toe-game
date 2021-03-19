# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:39:17 2021

@author: Samuel
"""

def func(x):
    return sqrt(x)

def numthod(a,b):
    if (func(a)*func(b))<0:
        c = a
        while (b-a)>=0.01:
            c = (a+b)/2
            if func(c)==0.0:
                break
            if (func(c)*func(a))<0:
                b = c
            else:
                a = c
    else:
        print("wrong a and b")
        return
    
    print("The value of the root is",c)


