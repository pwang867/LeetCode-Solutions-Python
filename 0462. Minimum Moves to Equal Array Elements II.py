# method 2, time O(1), same idea as best meeting point, just choose the median



# method 1, O(n), the final number must be from nums, so try nums[i] one by one
# we can get the moves of choosing nums[i] based on the moves of nums[i-1]
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        res = sum(nums) - nums[0]*len(nums)
        cur = res
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            cur += i*diff - (len(nums)-i)*diff
            res = min(res, cur)
        return res


"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""
