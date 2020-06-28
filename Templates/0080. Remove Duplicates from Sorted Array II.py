# two pointers, O(n)
# compare nums[right] == nums[left-2]


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        
        end = 2  # end is not checked yet
        for i in range(2, len(nums)):
            # if not (nums[i] == nums[end-1] and nums[i] == nums[end-2]):
            if nums[i] != nums[end-2]:  # simplified from the sentence above
                nums[end] = nums[i]
                end += 1
        
        return end


"""
Given a sorted array nums, remove the duplicates in-place such that duplicates 
appeared at most twice and return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
"""
