# time O(10^2n), space O(1)
# an math trick is used: the answer must be with length 2*n, at least for n <= 8


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        low, high = 10 ** (n - 1), 10 ** n - 1
        for left_half in xrange(high, low + 1, -1):   # using range() will result in MLE
            s_left_half = str(left_half)
            num = int(s_left_half + s_left_half[::-1])
            if self.is_palindrome(num, max(low, num // high),
                                  min(high, num // low, int(num ** 0.5))):
                return num % 1337

    def is_palindrome(self, num, low, high):
        for x in xrange(low, high + 1):
            if num % x == 0:
                return True
        return False


"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

 

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

 

Note:

The range of n is [1,8].
"""
