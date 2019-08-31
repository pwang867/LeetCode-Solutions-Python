# method 1, dp
# dp[i][j] means if s[:i] matches with p[:j]
# dp's dimension is (m+1)*(n+1) to consider empty string
# equation: when p[j-1] is "*" or is not "*"
# dp[i][j] = (s[i-1]==p[j-1] or p[j-1]=="?") and dp[i-1][j-1]
# dp[i][j] = dp[i][j-1] or (i>0 and dp[i-1][j])

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] != "*":
                    dp[i][j] = i>0 and (s[i-1]==p[j-1] or p[j-1]=="?") \
                                and dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1] or (i>0 and dp[i-1][j])
        
        return dp[m][n]
    
