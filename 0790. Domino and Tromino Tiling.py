# method 2: simplified from method 1, dp
# dp[i] = dp[i-1] + dp[i-2] + (dp[i-3] + ... + dp[0])*2
# can be simplified to dp[i] = 2*dp[i-1] + dp[i-3]
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 1:
            return 0
        if N < 3:
            return N
        
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, N+1):
            dp[i] = 2*dp[i-1] + dp[i-3]
            dp[i] %= 10**9+7
        
        return dp[N]
    

# method 1: dp
class Solution1(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return 1
        
        dp = [0]*(N+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
            j = i - 3
            while j >= 0: # tromino-(domino)^(2*m)-trimino
                dp[i] += 2*dp[j]
                j -= 2
            j = i -4
            while j >= 0:  # tromino-(domino)^(2*m+1)-trimino
                dp[i] += 2*dp[j]
                j -= 2
            dp[i] %= 10**9+7
        
        return dp[N]
    
        
