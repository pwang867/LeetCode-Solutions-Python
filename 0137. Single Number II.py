# https://leetcode.com/problems/single-number-ii/discuss/43295
# /Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1, x2 = 0, 0
        mask = 0
        for num in nums:
            x2 ^= (x1&num)
            x1 ^= num
            mask = ~(x2&x1)
            x2 = x2&mask
            x1 = x1&mask
        return x1|x2  # or return x1


"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""
