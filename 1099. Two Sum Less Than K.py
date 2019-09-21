class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        
        maxSum = float('inf')
        diff = float('inf')
        
        left, right = 0, len(A)-1
        while left < right:
            cur = A[left] + A[right]
            if cur < K and K-cur < diff:
                maxSum = cur
                diff = K-cur
            if cur < K:
                left += 1
            elif cur >= K:  # handle cur == K properly
                right -= 1
                
        return maxSum if maxSum != float('inf') else -1
    
