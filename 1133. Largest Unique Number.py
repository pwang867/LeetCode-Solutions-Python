# simple hashmap, time/space O(n)
from collections import Counter


class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = Counter(A)
        max_int = -float('inf')
        for key, val in d.items():
            if val == 1:
                max_int = max(max_int, key)
        return max_int if max_int != -float('inf') else -1


"""
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 

Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
 

Note:

1 <= A.length <= 2000
0 <= A[i] <= 1000
"""