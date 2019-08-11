class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # corner cases
        if z == 0:
            return True
        if x == 0:
            return z == y
        if y == 0:
            return z == x
        
        gcd_xy = self.gcd(x, y)
        
        return z >= 0 and z <= x+y and z%gcd_xy == 0
    
    def gcd(self, x, y):
        # find the greatest common factor (gcd) of positive integers x and y
        # x > 0 and y > 0
        if x < y:
            x, y = y, x
        while True:
            temp = x%y
            if temp == 0:
                return y
            x, y = y, temp
        
