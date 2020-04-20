# method 1, Hashtable, time/space O(n)


class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_sums = collections.defaultdict(int)
        for i in range(1, n + 1):
            digit_sum = self.get_digit_sum(i)
            digit_sums[digit_sum] += 1
        max_size = max(digit_sums.values())
        cnt = 0
        for freq in digit_sums.values():
            if freq == max_size:
                cnt += 1
        return cnt

    def get_digit_sum(self, num):
        res = 0
        while num > 0:
            res += num % 10
            num //= 10
        return res


# method 2
def countLargestGroup(self, n):
    return len(statistics.multimode(sum(map(int, str(i))) for i in range(1, n+1)))


"""
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.



Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
Example 3:

Input: n = 15
Output: 6
Example 4:

Input: n = 24
Output: 5


Constraints:

1 <= n <= 10^4
"""