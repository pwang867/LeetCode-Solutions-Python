# method 2: O(m*n)
"""
# dp[i][j] means if s[:i] matches with p[:j]
# two conditions. 
# 1. p[i-1] is not "*", then:
# dp[i][j] = (s[i-1]==p[j-1] or p[j-1]==".") and dp[i-1][j-1]
# 2. p[i-1] is "*", then matches with nothing or several s[i-1]: 
# dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=="."))
"""
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
                if j == 1:  # mistake: dp[i][j] == i-1 and...
                    dp[i][j] = i==1 and (s[i-1]==p[j-1] or p[j-1]==".")
                elif p[j-1] != "*":  # easy to forget i > 0
                    dp[i][j] = i>0 and (s[i-1]==p[j-1] or p[j-1]==".") \
                                and dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-2] or (i>0 and dp[i-1][j] \
                                              and (s[i-1]==p[j-2] or p[j-2]=="."))
        
        return dp[m][n]
    


# recursion with memo, time O(m*n)
# p only has three conditions: 1. a letter, 2. ".", 3. a letter for "." combined with "*"
# "*" is never used alone, and has to be used with a previous letter

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.memo = {}  # save failed match
        return self.isMatchHelper(s, p, 0, 0)
    
    def isMatchHelper(self, s, p, i, j):
        # compare s[i:] and p[j:]
        if (i,j) in self.memo:
            return self.memo[(i,j)]  # or return False
        
        # to make sure s[i] and p[j] are valid
        if j >= len(p):
            # mistake: return self.memo[(i,j)] = (i >= len(s))
            # Python assignment doesn't return a value, unlike in C++
            self.memo[(i,j)] = i >= len(s)
            return self.memo[(i,j)]
        if i >= len(s):
            self.memo[(i,j)] = len(p)-j > 1 and p[j+1] == "*" \
                    and self.isMatchHelper(s, p, i, j+2)
            return self.memo[(i,j)]
        
        # to make sure p[j+1] is valid
        if j == len(p)-1:
            self.memo[(i,j)] = (i == len(s)-1 and (s[i]==p[j] or p[j]=="."))
            return self.memo[(i,j)]
        
        # general case
        if p[j+1] != "*":  # mistake: p[1] == "*"
            self.memo[(i,j)] = (s[i]==p[j] or p[j]==".") \
                    and self.isMatchHelper(s, p, i+1, j+1)
            return self.memo[(i,j)]
        else:
            if self.isMatchHelper(s, p, i, j+2):
                return True
            for k in range(i, len(s)):
                if (s[k] == p[j] or p[j] == "."):
                    if self.isMatchHelper(s, p, k+1, j+2):
                        return True
                else:
                    break
        
        self.memo[(i,j)] = False
        return False
    
