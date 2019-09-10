# method 3, reduce row and col one by one
# time O(m+n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False

# method2, binary search, time O(log(m*n))
# don't search on the diagonal, only check the matrix center
# and then drop 1/4 of the matrix
class Solution2(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        return self.binarySearch(matrix, target, 
                                 0, 0, len(matrix), len(matrix[0]))
    
    def binarySearch(self, matrix, target, i, j, p, q):
        if i > p or j > q or i >=len(matrix) \
            or j >= len(matrix[0]) or p < 0 or q < 0:
            return False
        
        x, y = (i+p)//2, (j+q)//2  # middle point of the matrix
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] > target:
            return self.binarySearch(matrix, target, i, j, p, y-1) or \
                   self.binarySearch(matrix, target, i, y, x-1, q)
        else:
            return self.binarySearch(matrix, target, x+1, j, p, y) or \
                   self.binarySearch(matrix, target, i, y+1, p, q)
        

# binary search, time O(log(m+n)*long(m*n))
class Solution1(object):
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
        # defined by topleft (i, j), bottomright (p, q)
        # then cut half of the matrix and recur in the 
        # bottom left and topright sub-matrix
        
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
        
        
