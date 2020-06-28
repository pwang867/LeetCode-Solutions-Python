# time log(x) + log(y)
# corner cases: 1. z == 0, 2. z > x + y

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
        if y == 0:
            return x
        return self.gcd(y, x%y)

"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""

