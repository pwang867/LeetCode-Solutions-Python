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
        for key, val in freq.items():  # now only two items are left
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



"""
Given an array nums of positive integers, 
return the longest possible length of an array prefix of nums, 
such that it is possible to remove exactly one element 
from this prefix so that every number that has appeared in it 
will have the same number of occurrences.

If after removing one element there are no remaining elements, 
it's still considered that every appeared number has the same number of ocurrences (0).

 

Example 1:

Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, 
if we remove nums[4]=5, we will get [2,2,1,1,3,3], 
so that each number will appear exactly twice.
Example 2:

Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13
"""
