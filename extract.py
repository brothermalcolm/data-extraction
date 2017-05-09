# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:14:22 2017

@author: SERNMO
"""

#%% 
# Read file line by line
fhand = open('16112601.txt')
for line in fhand:
    print(line.rstrip().upper())
