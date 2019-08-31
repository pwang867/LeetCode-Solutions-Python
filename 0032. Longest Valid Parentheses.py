# method 2: dp[i] means the length of 
# the longest valid parentheses ending in s[i]
# method 2: dp, simplified from method 1 by using padding
class Solution(object):
    def longestValidParentheses(self, s):
        s = "##" + s
        dp = [0]*len(s)
        
        res = 0
        for i in range(2, len(s)):
            if s[i] == ")" and s[i-1-dp[i-1]] == "(":
                dp[i] = 2 + dp[i-1] + dp[i-2-dp[i-1]]
            res = max(res, dp[i])
        
        return res


# method 1: dp
class Solution1(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        dp = [0]*len(s)
        
        if s[1] == ")" and s[0] == "(":
            dp[1] = 2
        
        for i in range(2, len(s)):
            if i-1-dp[i-1]>=0 and s[i] == ")" and s[i-1-dp[i-1]] == "(":
                dp[i] = 2 + dp[i-1]
                if i-2-dp[i-1] >= 0:
                    dp[i] += dp[i-2-dp[i-1]]
        
        return max(dp)
        
