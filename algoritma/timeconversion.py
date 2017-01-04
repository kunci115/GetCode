# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:06:39 2016

@author: root
"""

import sys

time = raw_input().strip()
panjang = len(time)
if panjang > 8:
    
    a = int(time[0:2])
    b = time[8:10]
    if b == "AM":
        if a == 12:
            a = a - 12
            if a == 0:
                a = "00"
        if a == 1:
            a = "01"
        if a == 2:
            a = "02"
        if a == 3:
            a = "03"
        if a == 4:
            a = "04"
        if a == 5:
            a = "05"
        if a == 6:
            a = "06"
        if a == 7:
            a = "07"
        if a == 8:
            a = "08"
        if a == 9:
            a = "09"
    if b == "PM":
        if a < 12:
            a = a + 12
time = time[2:8]
    
    
print "{}{}".format(a,time)