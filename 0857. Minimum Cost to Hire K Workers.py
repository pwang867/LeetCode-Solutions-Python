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
        sums = [0]*n     # sums[i] = total_quality_of_smallest_K-1_workers in arr[:i]
        heap = [-arr[i][1] for i in range(K-1)]
        heapq.heapify(heap)
        total = sum(heap)    # total = - total_quality_of_K-1_workers
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
    
        
"""
There are N workers.  The i-th worker has a quality[i] and a 
minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  
When hiring a group of K workers, we must pay them according to 
the following rules:

Every worker in the paid group should be paid in the ratio of 
their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum 
wage expectation.
Return the least amount of money needed to form a paid group satisfying the 
above conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.
"""
