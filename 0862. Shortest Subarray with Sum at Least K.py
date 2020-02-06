# method 2, maintain an increasing deque, space O(res)
from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        queue = deque([[0, -1]])   # deque saves [presum, index]
        cur = 0
        res = float('inf')
        for i, a in enumerate(A):
            cur += a
            while queue and cur - queue[0][0] >= K:  
                res = min(res, i - queue.popleft()[1])
            while queue and cur <= queue[-1][0]:
                queue.pop()
            queue.append([cur, i])
        return res if res != float('inf') else -1


# method 1: brute force, O(n^2)


"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""
