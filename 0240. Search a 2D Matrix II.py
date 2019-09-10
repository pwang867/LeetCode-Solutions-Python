# method1, binary search 
# time O(log(m+n)*long(m*n))
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        return self.helper(matrix, 0, 0, m - 1, n - 1, target)
    
    def helper(self, matrix, i, j, p, q, target):
        # search in the diagonal of matrix 
        # topleft (i, j), bottomright (p, q)
        
        # find the size of diagonal
        m = p - i + 1
        n = q - j + 1
        size = min(m, n)
        if size == 1:
            return self.binarySearch(matrix, i, j, p, q, target)
        
        if matrix[i][j] == target:
            return True
        else:
            left = 0
        right = size  # not size - 1
        
        # binary search along the diagonal
        while left + 1 < right:
            mid = (left + right)/2
            if matrix[i + mid][j + mid] == target:
                return True
            elif matrix[i + mid][j + mid] > target:
                right = mid
            else:
                left = mid
        x, y = i + right, j + right 
        
        # recursively search the bottomleft and topright matrix
        if i <= x - 1 <= p and j <= y <= q:
            if self.helper(matrix, i, y, x - 1, q, target):
                return True
        if i <= x <= p and j <= y - 1 <= q:
            if self.helper(matrix, x, j, p, y - 1, target):
                return True
        return False
    
    def binarySearch(self, matrix, i, j, p, q, target):
        # search in 1D array
        if i == p:
            left, right = j, q
            while left + 1 < right:
                mid = left + (right - left)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid
                else:
                    left = mid
            return matrix[i][left] == target or matrix[i][right] == target
        
        if j == q:
            left, right = i, p
            while left + 1 < right:
                mid = left + (right - left)//2
                if matrix[mid][j] == target:
                    return True
                elif matrix[mid][j] > target:
                    right = mid
                else:
                    left = mid
            return matrix[left][j] == target or matrix[right][j] == target
        
        
