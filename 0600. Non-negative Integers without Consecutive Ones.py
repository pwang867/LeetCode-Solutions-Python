# dp[i][j] means the number of valid numbers starting with digit i having a length n-j
# time/space O(n), where n = log(num) = len(bin(num))


class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(bin(num)[2:])
        n = len(s)
        dp = [[0] * n for _ in range(2)]
        dp[0][n - 1] = 1
        dp[1][n - 1] = 1
        for j in range(n - 2, -1, -1):
            dp[0][j] = dp[0][j + 1] + dp[1][j + 1]
            dp[1][j] = dp[0][j + 1]
        res = 0
        for j in range(n):
            if s[j] == "1":
                res += dp[0][j]
                if j - 1 >= 0 and s[j - 1] == '1':
                    break
        else:
            res += 1  # num itself
        return res


"""
Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:
Input: 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
Note: 1 <= n <= 109
"""