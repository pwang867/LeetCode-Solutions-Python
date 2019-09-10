# method 2: binary search O(log(n))
# other methods: Newton's method
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
        
# method1, Newton's method, O(log(n))
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
    
