# method 2: based on method 1, time O(n), but reduce space to O(1)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        
        a, b = 1, 1
        for i in range(1, len(s)):
            temp = 0
            if s[i] != "0":
                temp += b
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += a
            if temp == 0:
                return 0
            a, b = b, temp
        
        return b
    


# method 1, dynamic programming, time O(n), space O(n)
# idea is easy, but be careful about dealing with "0"
# such as "0", "10", "301", etc
# dp[i] means the number of ways to decode s[:i]
# dp[i] = dp[i-1] + dp[i-2], be careful about the index
# similar to Fibonacci array
class Solution1(object):
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
    
