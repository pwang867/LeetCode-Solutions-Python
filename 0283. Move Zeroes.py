# time O(n), in place


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        end = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[end], nums[i] = nums[i], nums[end]
                # nums[end] = nums[i]   # those two lines are wrong solution, edge case: [1]
                # nums[i] = 0
                end += 1


"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
