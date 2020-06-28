import collections


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = collections.defaultdict(list)
        nums.sort()
        for i, num in enumerate(nums):
            if nums[i]-2 in d:
                return False
            if num-1 not in d:
                d[num].append(1)
            else:
                cnt = d[num-1].pop()
                if not d[num-1]:
                    del d[num-1]
                if cnt + 1 < k:
                    d[num].append(cnt+1)
        return len(d) == 0


"""
Given an array of integers nums and a positive integer k, 
find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
"""
