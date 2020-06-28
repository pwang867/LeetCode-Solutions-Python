# reservoir sampling
# space O(1), time O(n)


import random


class Solution(object):
    def __init__(self, nums):
        self.nums = nums
    
    def pick(self, target):
        count = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randrange(count) == 0:
                    res = i
        return res


# extra space O(n), time pick O(1)


import random
from collections import defaultdict


class Solution1(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.d = defaultdict(list)
        for i in range(len(nums)):
            self.d[nums[i]].append(i)
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target not in self.d:
            return -1
        indice = self.d[target]
        if len(indice) == 1:
            return indice[0]
        return random.choice(indice)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


if __name__ == "__main__":
    print(Solution([1, 2, 3, 3, 3]).pick(3))


"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
