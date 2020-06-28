# method 2, sliding window, time O(n), space O(1)


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        elif k > 0:
            return self.at_most(nums, k) - self.at_most(nums, k - 1)
        else:
            return self.at_most(nums, 0)

    def at_most(self, nums, k):
        # find the number of subarrays with at most k odd numbers
        # sliding window
        left = 0
        res = 0
        n_odd = 0
        for right, num in enumerate(nums):
            n_odd += num % 2
            while n_odd > k:
                n_odd -= nums[left] % 2
                left += 1
            res += right - left + 1
        return res


# method 1, treat even number as 0, odd number as 1,
# then the problem becomes count the subarrays whose sum is k
# time/space O(n)


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sums = {0: 1}
        res = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num % 2
            if cur_sum - k in pre_sums:
                res += pre_sums[cur_sum - k]
            pre_sums[cur_sum] = pre_sums.get(cur_sum, 0) + 1
        return res


"""
Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""