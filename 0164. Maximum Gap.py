# bucket sort, time O(n)
import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        _min, _max = min(nums), max(nums)
        n = len(nums)
        bucket_size = int(math.ceil((_max - _min)*1.0/(n-1)))  # math.ceil returns the integer as a float
        min_buckets = [float('inf')]*(n-1)
        max_buckets = [-float('inf')]*(n-1)
        
        for i, num in enumerate(nums):
            if num in [_min, _max]:
                continue
            j = (num - _min)//bucket_size
            min_buckets[j] = min(min_buckets[j], num)
            max_buckets[j] = max(max_buckets[j], num)
        
        pre = _min
        res = 0
        for i in range(n-1):
            if min_buckets[i] == float('inf'):  # empty bucket
                continue
            res = max(res, min_buckets[i] - pre)
            pre = max_buckets[i]
        res = max(res, _max - pre)
        
        return res


"""
Given an unsorted array, find the maximum difference between the successive 
elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""
