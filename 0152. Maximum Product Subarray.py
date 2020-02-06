class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # _max means the max product ending in nums[i] and includes nums[i]
        # _min means the min product ending in nums[i]
        _max, _min = nums[0], nums[0]
        res = _max  # global maximum product
        for i in range(1, len(nums)):
            candidates = [nums[i], nums[i]*_max, nums[i]*_min]  # don't forget nums[i] itself
            _max = max(candidates)  
            _min = min(candidates)
            res = max(res, _max)
        
        return res


   
"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
