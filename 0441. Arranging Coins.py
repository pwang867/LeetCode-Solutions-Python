# coding=utf-8

# method 2, binary search
# time O(log(res))


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left + 1 < right:
            mid = left + (right - left) // 2
            cnt = self.count_coins_for_height(mid)
            if cnt <= n:
                left = mid
            else:
                right = mid
        if self.count_coins_for_height(right) <= n:
            return right
        else:
            return left

    def count_coins_for_height(self, h):
        return h * (h + 1) // 2


# method 1, row by row
# time O(res)

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while res < n:
            res += 1
            n -= res
        return res


"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""

