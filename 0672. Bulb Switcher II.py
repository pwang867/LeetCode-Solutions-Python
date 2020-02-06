# method 2: use Math
"""
Note the four buttons as (a, b, c, d)
we can easily see a*b = c, a*c = b, b*c = a
so we can only have 8 operations: (None, a, b, c, d, a*d, b*d, c*d)
where None means no operation, or means the original state
when n < 3, (a, b, c, d) might become each other, so we need to consider separately
"""
class Solution(object):
    def flipLights(self, n, m):
        if n == 0 or m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if m == 1 else 4
        if n > 2:
            if m == 1:
                return 4
            elif m == 2:
                return 7  # easy to miss !!
            else:
                return 8


# method 1: brute force, use bit operations to simulate the buttons
# there is definitely no more than 2^n states, so there must be a period/cycle
# we can use a set to save the previous states to help find the cycle
class Solution1(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        pass
        
