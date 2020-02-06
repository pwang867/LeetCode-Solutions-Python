# dp, O(n)
# the idea is easy, but be very careful about index and padding
# and a lot of other details
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "*" else 9
        
        for i in range(1, len(s)):
            
            # single digit s[i]
            if s[i] == "*":
                dp[i+1] += 9*dp[i]  # mistake: dp[i+1] += 9
            elif s[i] != "0":
                dp[i+1] += dp[i]
                
            # two digit s[i-1]+s[i]
            if s[i-1] in "*1":
                if s[i] == "*":
                    dp[i+1] += 9*dp[i-1]  # "*" doesn't include "0"
                else:
                    dp[i+1] += dp[i-1]
            if s[i-1] in "*2":
                if s[i] == "*":
                    dp[i+1] += 6*dp[i-1]
                elif 0 <= int(s[i]) <= 6:
                    dp[i+1] += dp[i-1]
            
            if dp[i+1] == 0:  # do not miss! and mistake: dp[i] == 0
                return 0
            else:
                dp[i+1] = dp[i+1] % (10**9 + 7)
        
        return dp[-1]
    
    
