# time O(k*m*log(k)), k = len(nums), m = len(nums[i])
# space O(k)
# maintain the min and max of the current choice

import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        for i in range(n):
            if not nums[i]:
                return []
        min_heap = [(nums[i][0], i, 0) for i in range(n)]
        heapq.heapify(min_heap)
        cur_max = max([nums[i][0] for i in range(n)])
        res = [min_heap[0][0], cur_max]
        while min_heap:
            cur_min, i, j = heapq.heappop(min_heap)
            if cur_max - cur_min < res[1] - res[0]:
                res = [cur_min, cur_max]
            if j + 1 < len(nums[i]):
                heapq.heappush(min_heap, (nums[i][j + 1], i, j + 1))
                cur_max = max(cur_max, nums[i][j + 1])
            else:
                break
        return res


"""
You have k lists of sorted integers in ascending order. Find the smallest range that includes at 
least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

 

Example 1:

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
 

Note:

The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
"""

