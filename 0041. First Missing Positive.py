# standard one pass with swap, similar to remove duplicates in sorted array
# edge case: [1,2,...,n]
# time O(n), space O(1)


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # corner case n=0 and n=1 are taken care of later
        
        # switch nums[i] with nums[nums[i]-1] if nums[i] != nums[nums[i] - 1]
        i = 0
        while i < n:
            j = nums[i] - 1
            if 0 <= j < n and nums[i] != nums[j]:  # redundant: i != j, easy to miss: 0 <= j < n 
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        # check: nums[i] should be filled with i + 1
        for i in range(n):
            if nums[i] - 1 != i:
                return i + 1
        
        return n + 1  # easy to forget when nums are [1,2,...,n]


"""
Given an unsorted integer array, find the smallest missing positive 
integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
"""
