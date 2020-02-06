# method 1: use a dictionary/hashmap to save visited numbers, 
# time O(n), space O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        visited = {}  # {num: index}, visited elements
        
        for i, num in enumerate(nums):
            if target - num in visited:
                return [visited[target-num], i]
            else:
                visited[num] = i
        
        return []  # not found

    
# method 2: brute force, time O(n^2), space O(1)
# iterate every possible two nums
class Solution2(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

if __name__ == "__main__":
    nums = [2, 5, 8, 11, 15]
    target = 10
    print(Solution().twoSum(nums, target))  # [0, 2]
    
    