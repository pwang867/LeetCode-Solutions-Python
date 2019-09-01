# dynamic programming, O(n)
# idea is easy, but be careful about dealing with "0"
# such as "0", "10", "301", etc
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=="0":
            return 0
        
        dp = [0]*(len(s)+1)  # use padding
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != "0":
                dp[i+1] = dp[i]
            if 10 <= int(s[i-1:i+1]) <= 26:  # mistake: int(s[i-1:i+1]) <= 26
                dp[i+1] += dp[i-1]
            if dp[i] == 0:
                return 0
        return dp[-1]
    
