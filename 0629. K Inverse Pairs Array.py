# time O(n*k), space O(k)


class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0] * (k + 1) for _ in range(2)]
        dp[0][0] = 1
        N = 10 ** 9 + 7
        for i in range(1, n + 1):
            dp[i % 2][0] = 1
            for j in range(1, k + 1):
                dp[i % 2][j] = (dp[(i - 1) % 2][j] + dp[i % 2][j - 1]) % N
                if j - i >= 0:
                    dp[i % 2][j] -= dp[(i - 1) % 2][j - i]
                dp[i % 2][j] %= N
        return dp[n % 2][k]


# time/space O(n*k)


class Solution1(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        N = 10 ** 9 + 7
        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
                if j - 1 >= 0 and max(j - 1 - (i - 1), 0) < max(j - (i - 1), 0):  # max(j - 1 - (i - 1), 0) < max(j - (i - 1), 0)
                    dp[i][j] -= dp[i - 1][max(j - 1 - (i - 1), 0)]
                if dp[i][j] == 0:   # early termination, optimization
                    break
                dp[i][j] %= N
        return dp[n][k]


"""
Given two integers n and k, find how many different arrays consist of numbers from 1 to n 
such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, 
if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 109 + 7.

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: 
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
 

Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: 
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

Note:

The integer n is in the range [1, 1000] and k is in the range [0, 1000].
"""