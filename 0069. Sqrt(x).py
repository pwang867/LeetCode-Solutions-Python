# follow-up: what about float mySqrt(float x) ?
# use eps to limit the resolution


# method 2: binary search O(log(n))
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        
        left, right = 0, x
        while left + 1 < right:
            mid = left + (right - left) // 2
            t = mid*mid
            if t == x:
                return mid
            elif t > x:
                right = mid
            else:
                left = mid
        
        if right*right <= x:
            return right
        else:
            return left
        
        
# method1, Newton's method, O(log(n)), X(n+1) = Xn - f(Xn)/f'(Xn)
# x = sqrt(n), f(x) = x^2 - n
# f(x) is not sqrt(x) !!!
class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x < 2:
            return x
        
        i = x
        while i*i > x:
            i = (i + x//i)//2
        
        return i
    


"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
"""
