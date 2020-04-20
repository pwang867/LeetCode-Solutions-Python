# pancake, time O(n), in place
# similar to #186. Reverse Words in a String II


class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums
        k = k%len(nums)
        nums = self.reverse(nums, 0, len(nums) - 1)
        nums = self.reverse(nums, 0, k - 1)
        nums = self.reverse(nums, k, len(nums) - 1)
    
    def reverse(self, nums, left, right):
        # reverse nums between index left and right
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


# method 1
# use hint 4, cyclic-dependencies
# when n = 4, k = 2, index 0 and 2 will be a dead loop,
# so we need to remember our starting index for each cycle

class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        k %= len(nums)
        istart = 0
        icur = istart
        copy = nums[icur]
        for _ in range(len(nums)):
            j = (icur + k) % len(nums)  # next position to go
            copy, nums[j] = nums[j], copy
            icur = j
            if icur == istart:  # this cycle is done, go to next cycle
                istart += 1
                icur = istart
                if icur < len(nums):
                    copy = nums[icur]
                else:
                    break


"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
