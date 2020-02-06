# Dynamic programming
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut = [n-1]*n    # cut[i] means the minimum number of cuts to partition s[:i+1] to palindrome array
        pal = [[False]*n for _ in range(n)]  # pal[i][j] == True meaning s[i:j+1] is a palindrome
        cut[0] = 0
        for j in range(len(s)):
            for i in range(j + 1):
                pal[i][j] = (s[i]==s[j]) and (i+1 >= j-1 or pal[i+1][j-1])
                if pal[i][j]:
                    cut[j] = min(cut[j], cut[i-1] + 1) if i > 0 else 0
        return cut[-1]



"""
Given a string s, partition s such that every substring of the partition 
is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
