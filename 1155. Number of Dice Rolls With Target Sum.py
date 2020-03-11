# dp
# time O(d*f*target), space O(target)
class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        dp = [[0] * (1 + target) for _ in range(2)]  # rolling array
        dp[0][0] = 1
        N = 10 ** 9 + 7
        for i in range(1, d + 1):
            dp[i % 2] = [0] * (1 + target)  # mistake: dp[i%2][0] = 0
            for j in range(1, target + 1):
                for k in range(1, min(f, j) + 1):
                    if j - k >= 0:
                        dp[i % 2][j] = (dp[i % 2][j] + dp[(i - 1) % 2][j - k])
                    else:
                        break
        return dp[d % 2][target] % N


# time O(d*f*target), space O(d*target)
class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if target <= 0:
            return 0
        N = 10 ** 9 + 7
        dp = [[0] * d for _ in range(target + 1)]
        for i in range(1, min(f, target) + 1):  # easy to make mistake
            dp[i][0] = 1
        for i in range(1, 1 + target):
            for j in range(1, d):
                for k in range(1, f + 1):
                    if i - k >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - k][j - 1]) % N
        return dp[-1][-1]


"""
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""