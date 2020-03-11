# two pointers
class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        maxSum = -float('inf')
        
        left, right = 0, len(A)-1
        while left < right:
            total = A[left] + A[right]
            if total < K:
                maxSum = max(maxSum, total)
                left += 1
            elif total >= K:  # handle total == K properly
                right -= 1
                
        return maxSum if maxSum != -float('inf') else -1


"""
Given an array A of integers and integer K, 
return the maximum S such that there exists i < j with A[i] + A[j] = S 
and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
"""

