# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:14:22 2017

@author: SERNMO
"""

#%%
# Open file
fhand = open('16112601.txt')

#%% 
# Read file line by line
for line in fhand:
    print(line.rstrip().upper())
    
#%%
# Look for lines of the form 
fname = input('Enter filename: ')
fhand = open(fname)
import re
regex = '.*;;;(.*;[0-9];)'
count = 0
ftar = open('e'+fname, 'w')
ftar.truncate
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        data = re.findall(regex, line)
        #print(data)
        print(line)
        count = count + 1
        ftar.write(str(data[0])+'\n')
print('file %s had %i lines that matched %s' % (fname, count, regex))
