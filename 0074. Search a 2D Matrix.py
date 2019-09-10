# binary search, O(log(m*n))
# we can use binary search to search row first, and then col
# but can also use smart index to search once
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        
        left, right = 0, m*n-1
        while left + 1 < right:
            
            mid = left + (right - left)//2
            t = matrix[mid//n][mid%n]
            if t == target:
                return True
            elif t > target:
                right = mid
            else:
                left = mid
        
        return matrix[left//n][left%n] == target or \
                matrix[right//n][right%n] == target
    
    
