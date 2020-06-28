# similar to # 123. Best Time to Buy and Sell Stock III
# iterate on the middle block


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or len(nums) < 3*k:
            return []

        # get presum
        total = 0
        pre_sums = []
        for num in nums:
            total += num
            pre_sums.append(total)
        n = len(nums)

        # find the max_sum of a single k-size subarray in nums[:i+1]
        left = [[-1, -1] for _ in range(n)]  # [[index, max_sum]]
        cur = sum(nums[:k])
        left[k-1] = [0, cur]
        for i in range(k, n):
            cur += nums[i] - nums[i-k]
            if cur > left[i-1][1]:
                left[i] = [i-k+1, cur]
            else:
                left[i] = left[i-1]

        # find the max_sum of a single k-size subarray in nums[i:]
        right = [[-1, -1] for _ in range(n)]
        cur = sum(nums[-k:])
        right[-k] = [n-k, cur]
        for i in range(n-k-1, -1, -1):
            cur += nums[i] - nums[i+k]
            if cur >= right[i+1][1]:
                right[i] = [i, cur]
            else:
                right[i] = right[i+1]

        # find the result by iterating the starting index of middle block
        max_sum = -float('inf')
        res = []
        for mid in range(k, n-2*k+1):
            cur = left[mid-1][1] + right[mid+k][1] + pre_sums[mid+k-1] - pre_sums[mid-1]
            if cur > max_sum:
                max_sum = cur
                res = [left[mid-1][0], mid, right[mid+k][0]]
        return res


"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). 
If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
 

Note:

nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""
