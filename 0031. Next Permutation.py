# time O(n), space O(1)
# 1. search backwards until the first i that nums[i] < nums[i+1]
# 2. then change direction to travel right to find the last nums[j] > nums[i], binary search
# 3. swap nums[i] and nums[j] and reverse nums[i+1:]
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        
        # search backwards the first j that nums[j] < nums[j+1] 
        # return nums.reverse() is no such j is not found
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                break
        else:
            # nums is already the largest
            nums.reverse()
            return
        
        # binary search
        # change direction and search the rightmost target that nums[target] > nums[i]
        left, right = i+1, n-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] <= nums[i]:
                right = mid
            else:
                left = mid
        if nums[right] > nums[i]:
            target = right
        else:
            target = left
        nums[i], nums[target] = nums[target], nums[i]
        
        # reverse nums[i+1:] in place
        left = i + 1
        right = n - 1
        while (left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        

"""
Implement next permutation, which rearranges numbers into 
the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange 
it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column 
and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

