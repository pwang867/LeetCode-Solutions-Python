# method 1: use dictionary/hashmap, time O(n), space O(n)
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

    
# method 2: brute force, O(n^2)
class Solution2(object):
    def twoSum(self, nums, target):
        n = len(nums)
        if n < 2:
            return []
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return res
    
