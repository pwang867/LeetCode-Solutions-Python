class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int, x >= 0
        :rtype: int
        """
        # sqrt(x) = x has: x = 0, 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        left, right = 0, x
        while left + 1 < right:
            mid = (left + right)/2
            square = mid*mid
            if square == x:
                return mid
            elif square > x:
                right = mid
            else:
                left = mid
        return left
    
