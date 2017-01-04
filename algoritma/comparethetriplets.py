# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:29:09 2016

@author: root
"""

#!/bin/python

import sys

def allice():
    a0,a1,a2 = raw_input().strip().split(' ')
    a0,a1,a2 = [int(a0),int(a1),int(a2)]
def bob():
    b0,b1,b2 = raw_input().strip().split(' ')
    b0,b1,b2 = [int(b0),int(b1),int(b2)]

if allice > bob:
    print 1
elif bob < allice:
    print 1
