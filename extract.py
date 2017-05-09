# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:14:22 2017

@author: SERNMO
"""
  
#%%
# Import packages
import re

# Open file i/o
fname = input('Enter filename: ')
fhand = open(fname)
ftar = open('e'+fname, 'w')
ftar.truncate()

# Look for lines of the form 
regex = '.*;;;(.*;[0-9];)'
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        data = re.findall(regex, line)
        #print(data)
        #print(line)
        count = count + 1
        ftar.write(str(data[0])+'\n')
print('file %s had %i lines that matched %s' % (fname, count, regex))

# Close file i/o
ftar.close()
