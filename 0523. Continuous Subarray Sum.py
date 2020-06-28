# easy to make many small mistakes...


# if (x-y)%k == 0, then x%k - y%k == 0
# method 2: use cur_sum%k to change cur_sum to 0~k-1
# edge case: k==0
# time O(n), space O(k) when k!= 0 or O(n) when k==0


class Solution(object):
    def checkSubarraySum(self, nums, k):
        if not nums or len(nums) < 2:
            return False
        k = abs(k)
        # mistake: pre_sums = {0:-1, nums[0]:0}, nums[0] might be 0
        pre_sums = {0: -1}  # {sum: index}  
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            if k != 0:  # if k==0, we don't have to change cur
                cur %= k
            if cur not in pre_sums:
                pre_sums[cur] = i
            elif i - pre_sums[cur] > 1:  # subarray size >= 2
                return True
        return False


# method 1: dynamic programming, presum, time O(n*n), space O(n) or overwrite nums


class Solution1(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False
        pre_sums = [0]*(len(nums)+1)
        pre_sums[1] = nums[0]
        for i in range(1, len(nums)):
            pre_sums[i+1] = pre_sums[i] + nums[i]
            for j in range(i):
                temp = pre_sums[i+1] - pre_sums[j]
                if (k==0 and temp==0) or (k != 0 and temp%k==0):  # mistake: forget k == 0
                    return True
        return False


"""
Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray 
of size at least 2 that sums up to a multiple of k, 
that is, sums up to n*k where n is also an integer.


Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
Accepted
"""
