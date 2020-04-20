# https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109507/Java-96ms-DP-Solution-with-Detailed-Explanation

# time O(n^3), space O(n^2)

class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        memo = {}
        return self.dp(S, 0, len(S) - 1, memo)

    def dp(self, S, left, right, memo):
        if (left, right) in memo:
            return memo[(left, right)]
        if left > right:
            return 0
        elif right == left:
            return 1
        else:
            cnt = 0
            if S[left] != S[right]:
                cnt = self.dp(S, left + 1, right, memo) \
                      + self.dp(S, left, right - 1, memo) \
                      - self.dp(S, left + 1, right - 1, memo)
            else:
                # to count the number of S[right] within S[left+1:right]
                # to avoid duplicates
                low, high = left + 1, right - 1
                while low <= right and S[low] != S[right]:
                    low += 1
                while left <= high and S[high] != S[right]:
                    high -= 1
                if high < low:  # no S[right] within S[left+1:right]
                    cnt = self.dp(S, left + 1, right - 1, memo) * 2 + 2
                elif high == low:  # one
                    cnt = self.dp(S, left + 1, right - 1, memo) * 2 + 1
                else:  # >= 2
                    cnt = self.dp(S, left + 1, right - 1, memo) * 2 \
                          - self.dp(S, low + 1, high - 1, memo)
            memo[(left, right)] = cnt % (10 ** 9 + 7)
            return memo[(left, right)]


"""
Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input:
S = 'bccb'
Output: 6
Explanation:
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:
Input:
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation:
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
Note:

The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""