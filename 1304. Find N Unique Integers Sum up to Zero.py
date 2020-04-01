# method 2: [-4, -2, 0, 2, 4]
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return list(range(-n+1, n, 2))
    


# method 1: [-2, -1, 0, 1, 2]
class Solution1(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return []
        res = [0]*n
        num = n//2
        for i in range(n//2):
            res[i] = -num
            res[-i-1] = num
            num -= 1
        return res


"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000
"""
