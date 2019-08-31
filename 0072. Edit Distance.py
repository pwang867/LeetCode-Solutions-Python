# method 2: dp, simplified from method 1, with greedy
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]: # match directly (greedy)
                    dp[i][j] = dp[i-1][j-1]
                else:  
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[-1][-1]
    

# method 1: dynamic programming
class Solution1(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
                if word1[i-1]==word2[j-1]:  # insert and delete
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:  # replace or match
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
        
        return dp[-1][-1]
    
