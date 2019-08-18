# time O(m*n), use Stack
# this problem is based on 84. Largest Rectangle in Histogram
# Build a histogram for each row, each hist is built on the previous hist
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        hist = [0]*n
        max_area = 0
        
        for i in range(m):
            # update hist for each row
            for j in range(n):
                if matrix[i][j] == "0":  # important !
                    hist[j] = 0
                else:
                    hist[j] += 1
            
            max_area = max(max_area, self.maxAreaInHist(hist))
        
        return max_area
    
    def maxAreaInHist(self, heights):
        # refer to solution for LeetCode 84
        stack = []
        max_area = 0
        heights.append(0)
        
        for i, height in enumerate(heights):
            if stack and height <= heights[stack[-1]]:
                while stack and height <= heights[stack[-1]]:
                    h = heights[stack.pop()]
                    left = 0 if not stack else stack[-1] + 1
                    max_area = max(max_area, h*(i-left))
            stack.append(i)
        
        heights.pop()
        return max_area
    
