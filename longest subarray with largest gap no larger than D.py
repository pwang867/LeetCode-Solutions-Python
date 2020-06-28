"""
Given a array of integers, find the longest subarray,
in which difference between any two numbers is less than or
equal to D. Return the length of the subarray.

similar to sliding window maximum
"""

import collections


class Solution1:
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


class Solution2:
    def longest_subarray(self, nums, D):
        asc = collections.deque()   # for min
        des = collections.deque()   # for max
        left = 0
        max_len = 0
        cnt = 0   # total number of valid subarrays with max - min == D, not only the longest one
        for right, num in enumerate(nums):
            # update min
            while asc and nums[asc[-1]] >= num:
                asc.pop()
            asc.append(right)
            # update max
            while des and nums[des[-1]] <= num:
                des.pop()
            des.append(right)
            # check condition max - min <= D
            while nums[des[0]] - nums[asc[0]] > D:
                if des[0] < asc[0]:
                    left = des.popleft() + 1
                else:
                    left = asc.popleft() + 1
            max_len = max(max_len, right-left+1)
            if nums[des[0]] - nums[asc[0]] == D:
                cnt += min(asc[0], des[0]) - left + 1
            print("left {} max {} min {} right {} max_len {} cnt {}".format(left, des[0], asc[0], right, max_len, cnt))
        return max_len


if __name__ == "__main__":
    nums = [4, 8, 6, 5, 9, 7, 2, 3, 1]
    nums = [4, 4, 4, 4, 4, 4, 4, 4, 4]
    D = 0
    print(Solution2().longest_subarray(nums, D))
