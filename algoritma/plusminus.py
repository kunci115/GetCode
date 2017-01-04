# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:41:43 2016

@author: rino
"""

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
positive = 0
for number in arr:
    if number > 0:
        positive += 1
negative = 0
for numbers in arr:
    if numbers < 0:
        negative += 1
nol = 0
for numberss in arr:
    if numberss == 0:
        nol += 1
        
fp = float(positive) / float(n)
fn = float(negative) / float(n)
nol = float(nol) / float(n)
print fp
print fn
print nol        



        
