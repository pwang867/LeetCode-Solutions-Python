# method 3: Java use treemap



# method 2: sliding window, using bucket (dictionary)
# time O(n), space O(k)
class Solution2(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 1:
            return False
        
        window = {}  # {buket id: value}, the window
        # if values are assigned to the same bucket, then their difference are no more than t
        bucket_size = t + 1  
        for right in range(len(nums)):
            bucket = nums[right]/bucket_size
            if bucket in window:
                return True
            if bucket - 1 in window and abs(window[bucket - 1] - nums[right]) <= t:
                return True
            if bucket + 1 in window and abs(window[bucket + 1] - nums[right]) <= t:
                return True
            window[bucket] = nums[right]  # window[bucket] must be empty when reaching here
            if right - k >= 0:
                left = right - k
                del window[nums[left]/bucket_size]
        return False


# Brute force, Time limit exceeded
# Time: O(n*k), space O(1)
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        n = len(nums)
        for i in range(n - 1):  # mistake: range(n - k)
            for j in range(i + 1, i + 1 + k):
                if j < n and abs(nums[i] - nums[j]) <= t:
                    return True
        return False


"""
Given an array of integers, find out whether there are two distinct indices 
i and j in the array such that the absolute difference between nums[i] 
and nums[j] is at most t and the absolute difference between i and j 
is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""
