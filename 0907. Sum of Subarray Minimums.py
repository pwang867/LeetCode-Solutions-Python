# descending stack, similar to largest rectangle in histogram


class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.append(0)
        res = 0
        stack = []
        N = 10 ** 9 + 7
        for i, a in enumerate(A):
            while stack and A[stack[-1]] >= a:
                j = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                res += (j - left) * (right - j) * A[j]
                res %= N
            stack.append(i)
        return res


"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""