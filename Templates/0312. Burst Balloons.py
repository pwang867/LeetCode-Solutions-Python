# coding=utf-8
# the boundaries (nums[i-1] and nums[j+1] are burst later
# only after the all the balloons in nums[i:j+1]) are burst

# dp[i][j] means the coins you can collect for balloons nums[i:j+1]
# when you burst those balloons first
# order: bottom to up, left to right


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        
        nums.insert(0, 1)
        nums.append(1)
        
        dp = [[0]*(n+2) for _ in range(n+2)]  # mistake: [0]*(n+1)
        
        for i in range(n, 0, -1):  # bottom up
            for j in range(i, n+1):  # left to right
                for k in range(i, j+1):  
                    # nums[k] is the last balloon to burst for balloons nums[i:j+1]
                    dp[i][j] = max(dp[i][j], 
                          dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1])
        
        return dp[1][n]
    

# time O(n^3), space O(n^2), recursion, top down


class Solution1(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        self.dp = {}
        return self.dfs(nums, 0, len(nums)-1, 1, 1)
    
    def dfs(self, nums, i, j, left, right):
        if j < i:
            return 0
        if i == j:
            return nums[i]*left*right
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        res = 0
        for k in range(i, j+1):   # k is the last one to burst in nums[i:j]
            res = max(res, self.dfs(nums, i, k-1, left, nums[k]) + nums[k]*left*right \
                            + self.dfs(nums, k+1, j, nums[k], right))
        self.dp[(i, j)] = res
        return res


"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst balloon i you will get 
nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

