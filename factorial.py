# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:39:32 2019

@author: WEIMIN ZHOU
"""

N = 100

total = 0
cur = 1.0
for i in range(1, N+1):
    cur /= i
    total += cur

print(total)

