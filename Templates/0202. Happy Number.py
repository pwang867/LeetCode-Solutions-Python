# because 299 -> 2^2 + 9^2 + 9^2 = 166, 399->171, 
# we can see that when n >= 299, 
# n will always become smaller and 
# there must be a cycle when we iterate
# we can use a set to save all appeared numbers


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = self.transform(n)
    
    def transform(self, n):
        ans = 0
        while n > 0:
            ans += (n%10)**2
            n /= 10
        return ans


"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of
 the squares of its digits, and repeat the process until the number equals 1 
 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
 Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
