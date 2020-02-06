# use heap, and always pop out the smallest element
# time O(k*log(n))
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(h)
        
        res = 0
        while k > 0:
            res, i, j = heapq.heappop(h)
            if j+1 < len(matrix[0]):
                heapq.heappush(h, (matrix[i][j+1], i, j+1))
            k -= 1
        
        return res
        
