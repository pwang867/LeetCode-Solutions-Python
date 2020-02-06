# x should be sorted in front of y if int(x+y)-int(y+x) > 0
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        nums.sort(cmp=lambda x, y: -(int(x+y)-int(y+x)))
        res = "".join(nums)
        return res.lstrip("0") or "0"  # edge case: "001"



"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
"""
