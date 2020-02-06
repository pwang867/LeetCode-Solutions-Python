# can record parent to save space to O(n)

# method 1: dynamic programming, time O(n^2), space O(n^2)
# if the subset is sorted as A < B < C, then we must have C%B==0, B%C == 0 
# things will be a little more complex if num can be 0
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        nums.sort()
        dp = [[num] for num in nums]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
        
        res = []
        for subset in dp:
            if len(subset) > len(res):
                res = subset
        return res
    

"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""
