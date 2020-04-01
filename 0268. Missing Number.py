# method 2, bit manipulation, O(n)
# use those rules: x^x = 0, 0^x = x
# note: the method for this solution works because nums are distinct

class Solution(object):
    def missingNumber(self, nums):
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i
            res ^= num
        return res

    
# method 1: math, O(n)
class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)/2 - sum(nums)


"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
