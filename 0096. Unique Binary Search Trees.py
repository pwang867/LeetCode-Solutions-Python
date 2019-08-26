# method 2: dp
class Solution(object):
    def numTrees(self, n):
        if n < 2:
            return 1
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]


# method 1: recursion with memo
class Solution1(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {}
        return self.numTreesHelper(n)
    
    def numTreesHelper(self, n):
        if n <= 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        
        cnt = 0
        for i in range(n):
            left = self.numTreesHelper(i-0)
            right = self.numTreesHelper(n-1-i)
            cnt += left*right
        
        self.memo[n] = cnt
        return cnt
    
