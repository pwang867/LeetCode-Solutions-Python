# find the different bit of the two numbers, 
# and use that bit to divide the nums into two groups
# each group containing only one of the single number
# then we do xor for each of the group
# time O(n), space O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        for num in nums:
            total ^= num
        
        bit = total&(-total)  # the two targets must have different numbers in bit
        bitone = 0
        bitzero = 0
        
        for num in nums:
            if num&bit == bit:
                bitone ^= num
            else:
                bitzero ^= num
        
        return [bitone, bitzero]


"""
Given an array of numbers nums, in which exactly two elements appear 
only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. 
So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant space complexity?
"""

