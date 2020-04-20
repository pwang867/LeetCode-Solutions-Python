# transfer to another problem: find the length of longest palindromic subsequence
# time/space O(n^2), space can be optimized to O(n)


class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if not s:
            return True
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):  # mistake(wrong direction): range(n-1, i, -1)
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return len(s) - dp[0][n - 1] <= k


# method 1, time O(n^2*k), not optimal


class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return self.dfs(s, 0, len(s) - 1, k, {})

    def dfs(self, s, left, right, k, memo):
        if k < 0:
            return False
        if left >= right:
            return True
        key = (left, right, k)
        if key in memo:
            return memo[key]
        res = False
        if s[left] == s[right]:
            res = self.dfs(s, left + 1, right - 1, k, memo)
        else:
            res = k > 0 and (self.dfs(s, left + 1, right, k - 1, memo) or \
                             self.dfs(s, left, right - 1, k - 1, memo))
        memo[key] = res
        return res


"""
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
 

Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length
"""

