# method 5: based on method 4, reduce time complexity 
# time O((m-n)*n), space O(n)
# only use a single 1D array to save memory
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, m+1):
            # for j in range(min(i,n), 0, -1):  # mistake: range(i, 0, -1)
            for j in range(min(n, i), max(i-(m-n)-1, 0), -1):
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]
        
        return dp[-1]


# method 4: based on method 3, further reduce number of 1D array from two to one
# time O((m+1)*(n+1)), space O(n)
class Solution4(object):
    def numDistinct(self, s, t):         
        m, n = len(s), len(t)
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range(1, m+1):
            for j in range(min(n, i), -1, -1):
                dp[j] = dp[j] + dp[j-1]*(s[i-1]==t[j-1])
        return dp[-1]
        
# method 3: dp, based on method 2, only use a two 1D array to save memory
# time O((m+1)*(n+1)), space O(n)
class Solution3(object):
    def numDistinct(self, s, t):  
        m, n = len(s), len(t)
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range(1, m+1):
            pre = dp + []
            for j in range(1, min(n+1, i+1)):
                dp[j] = pre[j] + pre[j-1]*(s[i-1]==t[j-1])
        
        return dp[-1]
        
        
# method 2: dynamic programming, time and space O((m+1)*(n+1))
# dp[i][j] means Distinct Subsequences of s[:i] which equals t[:j]
# dimension of dp[][] is (m+1)*(n+1)
class Solution2(object):
    def numDistinct(self, s, t):        
        m, n = len(s), len(t)
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 1
        for j in range(1, n+1):
            dp[0][j] = 0
        for i in range(1, m+1):
            for j in range(1, min(i+1,n+1)):  
                # better than: for j in range(1, n+1)
                if s[i-1] == t[j-1]:  # don't use s[i] == t[j] due to padding !!!
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
    
        
# method 1: recursion with memo, time and space O((m-n+1)*n)
class Solution1(object):
    def numDistinct(self, s, t):
        if not t:
            return 1
        if not s:
            return 0
        
        memo = {}
        
        return self.numDistinctHelper(s, len(s)-1, t, len(t)-1, memo)
    
    def numDistinctHelper(self, s, i, t, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if j > i:
            return 0
        if j == -1:
            return 1
        
        if s[i] == t[j]:
            cnt = self.numDistinctHelper(s, i-1, t, j-1, memo) \
            + self.numDistinctHelper(s, i-1, t, j, memo)
        else:
            cnt = self.numDistinctHelper(s, i-1, t, j, memo)
        
        memo[(i, j)] = cnt
        return cnt
    
        
        
