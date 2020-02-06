class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if (i%2 == 0 and i-1 >= 0 and nums[i] > nums[i-1]) or \
            (i%2 == 1 and i-1 >= 0 and nums[i] < nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]



"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""
