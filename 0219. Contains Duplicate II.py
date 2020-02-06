# time O(n), space O(n)
# sliding window, using dictionary to save {num: index}
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        _dict = {}  # {number: latest index}
        for i in range(len(nums)):
            if nums[i] in _dict and i - _dict[nums[i]] <= k:
                return True
            else:
                _dict[nums[i]] = i
        
        return False

# method 2, save some space over method 1, but twice slower due to set.remove()
# sliding window using set, time O(n), space O(k)
class Solution2(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()     # size <= k, every element in window will be different
        for i, num in enumerate(nums):
            if num in window:   # duplicate found
                return True
            else:
                window.add(num)
                if i-k >= 0:
                    window.remove(nums[i-k])
        return False
    


"""
Given an array of integers and an integer k, find out whether there are 
two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
