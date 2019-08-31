# method 2, recursion with memo, time O(m*n)
class Solution(object):
    def isMatch(s, p):
        self.memo = set()
        return self.isMatchHelper(s, p, 0, 0)
    
    def isMatchHelper(self, s, p, i, j):
        if j == len(p):
            return i == len(s)
        if (i, j) in self.memo:
            return False
        
        if p[j] == "*":
            if self.isMatchHelper(s, p, i, j+1):
                return True
            for k in range(i+1, len(s)+1):
                if self.isMatchHelper(s, p, k, j+1):
                    return True
        else:
            if i < len(s) and (s[i]==p[j] or p[j]=="?") \
                    and self.isMatchHelper(s, p, i+1, j+1):
                return True
        
        self.memo.add((i, j))
        return False


# method 1, dp, time O(m*n)
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
    
