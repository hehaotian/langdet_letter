# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:48:30 2013

@author: haotianhe
"""

import re
import csv
import numpy as np
import math

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# We read all the 
lf_table = csv.reader(open('letter_frequencies.csv'))

s = raw_input('Please input any sentence you want to detect:\n')
s_letters = ''.join(re.findall('[a-z]', s.lower()))

index = []

for i in range(len(s_letters)):
    for j in range(26):
        if (s_letters[i] == alphabet[j]):
            index.append(j)

prob = dict( (lf_row[0], np.array([float(v) for v in lf_row[1:]]) / 100)
                                          for lf_row in lf_table
                                          if lf_row[0] != "letter")

print ""
print "The probability of this sentence as"

for key in prob.keys():
   lang = prob[key]
   logAdd = 0
   for t in range(len(index)):
       logAdd = logAdd + math.log(lang[index[t]])
   print key + ": ", logAdd