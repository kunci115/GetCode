#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 19:08:34 2016

@author: root
"""

balance = int(raw_input())
year = 0
interest = 0
persen = 0.06
print "Penanaman modal pada tahun ke",year," ",balance
while balance <= 20000:
    year = year + 1
    b = balance * persen
    balance = balance + b
    print "tahun ke ",year," ",balance