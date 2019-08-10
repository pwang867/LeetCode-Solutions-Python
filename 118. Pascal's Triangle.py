# dynamic programming, space O(n), time O(n^2)
# bottom up
# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        elif numRows == 1:
            return [[1]]
        
        res = [[1]]
        for i in range(1, numRows):
            vals = [1]
            for j in range(i-1):  # not range(i)
                vals.append(res[-1][j] + res[-1][j+1])
            vals.append(1)
            res.append(vals)
        
        return res
    
    
