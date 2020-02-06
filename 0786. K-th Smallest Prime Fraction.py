# use heap, time O(K*log(n))
import heapq
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        n = len(A)
        if K > n*(n-1)//2 or n==1:
            return []
        
        h = [(A[i]*1.0/A[n-1], i, n-1) for i in range(n-1)]
        i, j = 0, n-1
        while K > 0:
            val, i, j = heapq.heappop(h)
            if j-1 > i:
                heapq.heappush(h, (A[i]*1.0/A[j-1], i, j-1))
            K -= 1
        
        return [A[i], A[j]]
    
