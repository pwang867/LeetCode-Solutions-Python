# dp[i][j] means the coins you can collect for ballons nums[i:j+1] 
# when you burst those ballons first
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
                    # nums[k] is the last ballon to burst for ballons nums[i:j+1]
                    dp[i][j] = max(dp[i][j], 
                          dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1])
        
        return dp[1][n]
    
