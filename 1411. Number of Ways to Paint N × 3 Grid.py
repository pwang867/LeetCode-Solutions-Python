# dp, method 2, time O(n)
# simplified from method 1 using symmetry

class Solution2(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = 10 ** 9 + 7
        a123, a121 = 6, 6
        for i in range(n - 1):
            a123, a121 = (2 * a121 + 2 * a123) % N, (3 * a121 + 2 * a123) % N
        return (a123 + a121) % N


# dp, time O(n), the current row only depends on the top row

class Solution1(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        N = 10**9 + 7
        states = []
        for i in range(3):
            for j in range(3):
                if j == i:
                    continue
                for k in range(3):
                    if k == j:
                        continue
                    states.append((i, j, k))
        dp = {state: 1 for state in states}
        for _ in range(n-1):
            new_dp = {state: 0 for state in states}
            for state in new_dp:
                for pre_state in dp:
                    if state[0] != pre_state[0] and state[1] != pre_state[1] and state[2] != pre_state[2]:
                        new_dp[state] += dp[pre_state]
                        new_dp[state] %= N
            dp = new_dp
        return sum(dp.values())%N


"""

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214


Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""