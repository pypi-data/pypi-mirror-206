# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:57:00 2023

@author: malha
"""

def fact(n):
    fact = 1
    if(n<0): return "INVALID NUMBER"
    while(n>1):
        fact*=n
        n-=1
    return fact