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
    
    
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
"""
