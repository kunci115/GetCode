# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 14:27:12 2016

@author: root
"""

#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
print a