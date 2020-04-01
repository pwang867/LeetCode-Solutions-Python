# method 2, optimized from method 1, still greedy
# O(n)

class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A or len(A) < K:
            return 0
        flips = [0]*len(A)  # flips[i] means if the A[i] is fliped
        cur_flip = 0   # the number of flips for A[i-K+1:i] that can affect A[i]
        for i in range(len(A)-K+1):
            if (cur_flip%2) ^ A[i] == 0:
                flips[i] = 1   # we need to flip A[i]
                cur_flip += 1
            if i >= K-1:
                cur_flip -= flips[i-K+1]
        for i in range(len(A)-K+1, len(A)):
            if (cur_flip%2) ^ A[i] == 0:
                return -1
            cur_flip -= flips[i-K+1]
        return sum(flips)

    
# greedy, time limit exceeded
# proof: regard each flip as an operation, we can see that the order of flip doesn't matter
# therefore, we can flip the array from left to right
class Solution1(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        cnt = 0
        for i in range(len(A)-K+1):
            num = A[i]
            if num == 0:
                cnt += 1
                for j in range(K):   # reason for time limit exceeded
                    A[i+j] = 1^A[i+j]
        for i in range(len(A)-K, len(A)):
            if A[i] != 1:
                return -1
        return cnt
    

"""
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

 

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
 

Note:

1 <= A.length <= 30000
1 <= K <= A.length
"""
