# dp[i][j] means the number of permutations for S[:i+1] when the last number is j-th
# largest number. Note that the last number is j-th largest, instead of number j
# time/space O(n^2), space can be optimized to O(n)


class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        N = 10 ** 9 + 7
        n = len(S)
        dp = [[0] * (n + 1) for _ in range(n)]
        if S[0] == "D":
            dp[0][0] = 1
        else:
            dp[0][1] = 1
        for i in range(1, n):
            if S[i] == "D":
                for j in range(i, -1, -1):
                    dp[i][j] = (dp[i - 1][j] + dp[i][j + 1]) % N
            else:
                for j in range(1, i + 2):
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % N
        return sum(dp[-1]) % N


"""
We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.



Example 1:

Input: "DID"
Output: 5
Explanation:
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)


Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}.
"""
