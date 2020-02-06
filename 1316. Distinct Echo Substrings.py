# rolling hash
# time/pace O(N^3) due to saving res
class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        if not text:
            return 0
        
        # calculate rolling hash, dp[i][j] is the hash for text[i:j+1]
        PRIME = 29
        N = 10**9 + 7
        n = len(text)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = ord(text[i]) - ord('a') + 1
            for j in range(i+1, n):
                dp[i][j] = (dp[i][j-1]*PRIME + ord(text[j]) - ord('a') + 1)%N
        
        # find echo strings
        res = set()
        for i in range(n):
            for j in range(i+1, n):
                if n-j < j-i:
                    break
                _len = j - i
                if dp[i][j-1] == dp[j][j+_len-1]:
                    res.add(text[i:j])
        return len(res)




"""
Return the number of distinct non-empty substrings of 
text that can be written as the concatenation of some string with 
itself (i.e. it can be written as a + a where a is some string).

 

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
 

Constraints:

1 <= text.length <= 2000
text has only lowercase English letters.
"""
