"""
Given a array of integers, find the longest subarray,
in which difference between any two numbers is less than or
equal to D. Return the length of the subarray.

similar to sliding window maximum
"""

import collections


class Solution:
    def longest_subarray(self, nums, D):
        max_len = 0
        dec = collections.deque([])   # save index
        inc = collections.deque([])
        left = 0
        for right, num in enumerate(nums):
            # increasing deque
            while inc and abs(nums[inc[0]]-num) > D:  # update left
                j = inc.popleft()
                left = max(left, j+1)
            while inc and nums[inc[-1]] >= num:    # maintain decreasing deque
                inc.pop()
            inc.append(right)
            # decreasing deque
            while dec and abs(nums[dec[0]]-num) > D:
                j = dec.popleft()
                left = max(left, j+1)
            while dec and nums[dec[-1]] <= num:
                dec.pop()
            dec.append(right)
            max_len = max(right-left+1, max_len)
        return max_len


if __name__ == "__main__":
    nums = [4, 8, 6, 5, 9, 7, 2, 3, 1]
    D = 2
    print(Solution().longest_subarray(nums, D))
