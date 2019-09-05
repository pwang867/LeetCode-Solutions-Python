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
    
