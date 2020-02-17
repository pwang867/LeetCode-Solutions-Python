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
    


"""
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]
Note:

A will have length between 2 and 2000.
Each A[i] will be between 1 and 30000.
K will be between 1 and A.length * (A.length - 1) / 2.
"""
