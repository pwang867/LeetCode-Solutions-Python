# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:29:01 2019

@author: WEIMIN ZHOU
"""

from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = Counter(arr)
        cnts = d.values()
        return len(cnts) == len(set(cnts))

print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))