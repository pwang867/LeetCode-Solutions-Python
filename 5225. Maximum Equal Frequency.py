# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:41:07 2019

@author: WEIMIN ZHOU
"""
from collections import Counter
class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = Counter(nums)
        for i in range(len(nums)-1, -1, -1):
            if i < 2:
                return i + 1
            if self.isValid(d):
                return i+1
            d[nums[i]] -= 1
            if d[nums[i]] == 0:
                del d[nums[i]]
    
    def isValid(self, d):
        freq = Counter(d.values())
        if len(freq) >= 3:
            return False
        if len(freq) <= 1:
            return freq.keys()[0] == 1 or freq.values()[0] == 1
        arr = []
        for key, val in freq.items():
            arr.append(key)
            arr.append(val)
        if arr[1] != 1 and arr[3] != 1:
            return False
        if arr[1] == 1 and arr[3] != 1:
            return arr[0] == 1 or arr[0] == arr[2] + 1
        if arr[3] == 1 and arr[1] != 1:
            return arr[2] == 1 or arr[2] == arr[0] + 1
        if arr[3] == 1 and arr[1] == 1:
            return arr[2] == 1 or arr[0] == 1 or abs(arr[0]-arr[2])==1
            
nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
print(Solution().maxEqualFreq(nums))

