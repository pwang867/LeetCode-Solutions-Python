class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left + 1 < right:
            mid = left + (right - left)//2
            square = mid*mid
            if square == num:
                return True
            elif square > num:
                right = mid
            else:
                left = mid
        return left*left == num or right*right == num


"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

