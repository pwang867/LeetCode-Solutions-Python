# dfs, time/space O(res)


class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        if low <= 0 <= high:
            res.append(0)
        for digit in range(1, 10):
            self.dfs(digit, digit, low, high, res)
        return sorted(res)

    def dfs(self, num, pre, low, high, res):
        if num > high:
            return
        if low <= num <= high:
            res.append(num)
        for x in [pre - 1, pre + 1]:
            if 0 <= x <= 9:
                self.dfs(num * 10 + x, x, low, high, res)


class Solution2:
    def get_counts_of_stepping_numbers(self, low, high):
        # only count the numbers, don't have to list them
        n = len(str(high))
        dp = self.build_dp(n)
        return self.below(high+1, dp) - self.below(low, dp)

    def below(self, num, dp):
        # get counts < num
        if num <= 0:
            return 0
        if num <= 10:
            return num
        num = str(num)[::-1]
        n = len(str(num))
        cnt = 1  # count 0
        for i in range(1, n):              # count numbers with length shorter then num
            for j in range(1, 10):
                cnt += dp[i][j]
        for j in range(1, int(num[-1])):   # same length but first digit smaller than num
            cnt += dp[n][j]
        for i in range(n-1, 0, -1):        # same length as num, first digit same as num
            digit = int(num[i-1])
            predigit = int(num[i])
            for j in [predigit-1, predigit+1]:   # for all candidates
                if 0 <= j < digit:               # compare with current digit
                    cnt += dp[i][j]
            if abs(digit - predigit) != 1:       # check whether keep going or not
                break

        return cnt

    def build_dp(self, n):
        dp = [[0] * 10 for _ in range(n+1)]
        dp[1] = [1]*10
        for i in range(2, n+1):
            for j in range(10):
                if j == 0:
                    dp[i][j] = dp[i-1][j+1]
                elif j == 9:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        return dp


for low, high in [(0, 50), (14, 50), (121, 500)]:
    print("low, high: ", low, high)
    print(Solution().countSteppingNumbers(low, high))
    print(Solution2().get_counts_of_stepping_numbers(low, high))
    print('\n')


"""
A Stepping Number is an integer such that all of its adjacent digits have an absolute difference of exactly 1. For example, 321 is a Stepping Number while 421 is not.

Given two integers low and high, find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.



Example 1:

Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]


Constraints:

0 <= low <= high <= 2 * 10^9
"""