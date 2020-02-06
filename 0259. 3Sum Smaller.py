# time O(n^2), space O(1)
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0
        
        nums.sort()  # needs to check if nums is already sorted
        count = 0
        for i in range(len(nums)-3+1):
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] >= target:
                    right -= 1
                else:
                    count += right-left
                    left += 1
        
        return count

"""
Given an array of n integers nums and a target, find the number 
of index triplets i, j, k with 0 <= i < j < k < n that 
satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
"""
