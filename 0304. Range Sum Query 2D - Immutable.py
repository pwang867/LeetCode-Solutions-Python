class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sums = matrix + []
        
        if matrix and matrix[0]:
            m, n = len(matrix), len(matrix[0])
            for i in range(m):
                for j in range(n):
                    self.sums[i][j] += self.getSum(i-1, j) + self.getSum(i, j-1) \
                                        - self.getSum(i-1,j-1)
    
    def getSum(self, i, j):  # to make self.sums initialization and range sum query easy
        if not self.sums or not self.sums[0]:
            return 0
        if i < 0 or i >= len(self.sums) or j < 0 or j >= len(self.sums[0]):
            return 0
        return self.sums[i][j]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getSum(row2, col2) + self.getSum(row1-1, col1-1) \
                - self.getSum(row1-1, col2) - self.getSum(row2, col1-1)
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
