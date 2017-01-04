# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:23:16 2016

@author: root
"""

mealcost = float(raw_input())
tippercent = int(raw_input())
taxpercent = int(raw_input())

tip = (mealcost * tippercent) / 100
tax = (mealcost * taxpercent) / 100
totalCost = mealcost + tip + tax

a = round(totalCost)
b= int(totalCost)
print 'The total meal cost is',b, 'dollars.'