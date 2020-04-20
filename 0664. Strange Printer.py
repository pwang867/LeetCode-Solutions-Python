# dp[i][j] means the number of turns to print s[i:j+1]
# time O(n^3), space O(n^2)
# dp[i][j] means the number of turns to print s[i:j+1]
# time O(n^3), space O(n^2)

# method 2, optimized from method 1, complexities are the same


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        short_s = []
        for c in s:   # optimization 1, reduce consecutive chars to a single one
            if not short_s or short_s[-1] != c:
                short_s.append(c)
        s = "".join(short_s)
        self.memo = {}
        return self.dp(s, 0, len(s) - 1)

    def dp(self, s, left, right):
        if left > right:
            return 0
        elif left == right:
            return 1
        key = (left, right)
        if key in self.memo:
            return self.memo[key]
        nturns = self.dp(s, left, right - 1) + 1  # when s[right] is printed by itself
        for i in range(left, right):  # when s[right] is printed together with char in other locations
            if s[i] == s[right]:  # optimization 2
                nturns = min(nturns, self.dp(s, left, i) + self.dp(s, i + 1, right - 1))  # right - 1 is important
        self.memo[key] = nturns
        return nturns


# method 1, dp
class Solution1(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.memo = {}
        return self.dp(s, 0, len(s) - 1)

    def dp(self, s, left, right):
        if left > right:
            return 0
        elif left == right:
            return 1
        key = (left, right)
        if key in self.memo:
            return self.memo[key]
        nturns = right - left + 1
        # when s[left] and s[right] are printed separately
        for i in range(left, right):
            nturns = min(nturns, self.dp(s, left, i) + self.dp(s, i + 1, right))
        # when s[left] and s[right] and printed in one turn
        if s[left] == s[right]:
            nturns = min(nturns, self.dp(s, left + 1, right))
        self.memo[key] = nturns
        return nturns


"""
There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.
"""