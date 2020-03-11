# method 2: binary search, O((m+n)*log(max_num)), space O(1)
# edge case: [[1,2],[1,3]], k=1, self.count(matrix, 1) == 2
# easy to have bugs

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0] or k > len(matrix)*len(matrix[0]):
            return None
        left, right = matrix[0][0], matrix[-1][-1]
        while left + 1 < right:
            mid = left + (right-left)//2
            cnt = self.count(matrix, mid)   # find counts of numbers in matrix <= mid
            if cnt >= k:    # mistake: if cnt == k: return mid
                right = mid
            else:
                left = mid
        if self.count(matrix, left) >= k:   # mistake: if self.count(matrix, left) == k
            return left
        return right
    
    def count(self, matrix, target):
        # count the number of elements in matrix <= target
        cnt = 0
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] <= target:
                cnt += j + 1
                i += 1
            else:
                j -= 1
        return cnt


# method 1, use heap, and always pop out the smallest element
# time O(k*log(n))
import heapq
class Solution1(object):
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


"""        
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
