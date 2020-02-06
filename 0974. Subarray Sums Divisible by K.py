# similar but much easier than problem # 523 Continous Subarray Sum

# pre sums, time O(n), space O(n)
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if K == 0:
            return 0
        K = abs(K)
        
        res = 0
        sums = {0: 1}
        cur = 0
        for num in A:
            cur += num
            cur %= K
            res += sums.get(cur, 0)
            sums[cur] = sums.get(cur, 0) + 1
        return res



"""
974. Subarray Sums Divisible by K
Medium

456

41

Favorite

Share
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""
