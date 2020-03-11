# binary search, and rolling hash, O(N*log(N))
class Solution(object):
    def longestRepeatingSubstring(self, S):
        left, right = 0, len(S)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.hasRepeat(S, mid):
                left = mid
            else:
                right = mid
        return left

    def hasRepeat(self, S, length):
        # rolling hash: abc = a*29^2 + b*29^1 + c*29^0
        d = {}  # hash value: start index
        hash_val = 0
        base = 29
        N = 10 ** 9 + 1
        for i in range(length):
            hash_val = (hash_val * base + ord(S[i]) - ord('a') + 1) % N
        d[hash_val] = 0
        factor = base ** (length - 1)
        for i in range(1, len(S) - length + 1):
            hash_val -= (ord(S[i - 1]) - ord('a') + 1) * factor
            hash_val = ((hash_val * base) % N + ord(S[i + length - 1]) - ord('a') + 1) % N
            if hash_val in d and self.match(S, i, d[hash_val], length):
                return True
            else:
                d[hash_val] = i
        return False

    def match(self, S, i, j, length):
        for k in range(length):
            if S[i + k] != S[j + k]:
                return False
        return True


# dynamic programming, time/space O(N^2)
class Solution2(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        n = len(S)
        dp = [[0] * n for _ in range(n)]  # can be reduced to 1D
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if S[i] == S[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res


# binary search, time O(N^2*log(N))
class Solution1(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        left, right = 0, len(S)  # the length of the res
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.hasRepeat(S, mid):
                left = mid
            else:
                right = mid
        return left

    def hasRepeat(self, S, length):
        strs = set()
        for i in range(len(S) - length + 1):
            s = S[i:i + length]
            if s in strs:
                return True
            else:
                strs.add(s)
        return False


"""
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.



Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.


Note:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500
"""