class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:  # easy to miss!!!
            return nums[0]
        
        # cut a circle into two 1DArrays without circles
        max1 = self.rob1DArray(nums[1:])
        max2 = self.rob1DArray(nums[:-1])
        return max(max1, max2)
    
    def rob1DArray(self, nums):
        # refer to LeetCode 198. House Robber
        if not nums:
            return 0
        pre1, pre2 = 0, 0
        for i in nums:
            pre1, pre2 = pre2, max(pre2, pre1 + i)
        return pre2
    
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
