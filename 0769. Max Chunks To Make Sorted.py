# method 2, use the fact that the arr is a permutation of 0 ~ n-1
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = 0
        cur = -float('inf')
        for i, num in enumerate(arr):
            cur = max(cur, num)
            if cur == i:
                cnt += 1
        return cnt
    

# method 1, line sweep, time/space O(n)
# this method doesn't depend on the value of arr
class Solution1(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        n = len(arr)
        
        max_val = [0]*n  # max_val is the max of arr[:i+1]
        cur = -float('inf')
        for i, num in enumerate(arr):
            cur = max(cur, num)
            max_val[i] = cur
        
        min_val = [0]*n  # min_val is the min of arr[i:]
        cur = float('inf')
        for i in range(n-1, -1, -1):
            cur = min(cur, arr[i])
            min_val[i] = cur
        
        cnt = 0
        for i in range(n):
            if i == n-1 or max_val[i] < min_val[i+1]:
                cnt += 1
        return cnt

"""
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
"""
