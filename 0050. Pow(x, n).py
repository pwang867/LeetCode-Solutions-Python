# method 1: binary search, recursion


class Solution1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.myPow(x, -n)
        
        half = self.myPow(x, n//2)
        if n % 2 == 0:
            return half*half   # will cause overflow if we use half**2 (reason unknown)
        else:
            return half*half*x


# method 2: binary search, iteration
# x**(2*n+1) = x*(x**2)**2
class Solution(object):
    def myPow(self, x, n):
        if x == 1 or n == 0:
            return 1
        if x == 0:
            return 0
        
        res = 1
        i = n if n > 0 else -n
        while i != 0:
            if i % 2 == 1:
                res *= x
            x = x*x
            i = i>>1
        
        if n < 0:
            return 1.0/res
        else:
            return res
        
