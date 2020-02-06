# method 2, sliding window using two pointers, time O(n), space O(1)
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        cnt_zeros = 0
        left, right = 0, 0
        for right, num in enumerate(A):
            if num == 0:
                cnt_zeros += 1
                while cnt_zeros > K:
                    if A[left] == 0:
                        cnt_zeros -= 1
                    left += 1
            res = max(res, right-left+1)
        return res


# method 1, sliding window using a deque, time O(n), space O(res)
from collections import deque
class Solution1(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        queue = deque()    # queue records the index of 0 within the sliding window
        res = 0
        left = 0
        for right, num in enumerate(A):
            if A[right] == 0:
                queue.append(right)
                if len(queue) > K:
                    left = queue.popleft() + 1
            res = max(res, right-left+1)
        return res



"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
"""
