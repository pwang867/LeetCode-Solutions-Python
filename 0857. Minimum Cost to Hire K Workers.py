# time O(n*log(n)), space O(n)
# 1. sort the workers by ratio of wage/quality
# 2. the cost for the choice with worker arr[i] 
# as the highest ratio worker will be the sum of qualities 
# of the first k-1 workers within arr[:i] with smallest quality
# plus the worker arr[i], and then multiply the ratio of arr[i]

import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        if K > len(quality):
            return -1
        if K == 1:
            return min(wage)
        
        # sort workers by wage/quality ratio
        n = len(quality)
        arr = [(wage[i]*1.0/quality[i], quality[i]) for i in range(n)]
        arr.sort()
        
        # use a heap to help find the smallest sum of qualities 
        # when choosing K-1 workers within arr[:i]
        sums = [0]*n
        heap = [-arr[i][1] for i in range(K-1)]
        heapq.heapify(heap)
        total = sum(heap)
        sums[K-2] = -total
        for i in range(K-1, n):
            heapq.heappush(heap, -arr[i][1])
            total += -arr[i][1]
            total -= heapq.heappop(heap)
            sums[i] = -total
        
        minCost = float('inf')
        for i in range(K-1, n):
            minCost = min(minCost, arr[i][0]*(arr[i][1]+sums[i-1]))
        
        return minCost
    
        
