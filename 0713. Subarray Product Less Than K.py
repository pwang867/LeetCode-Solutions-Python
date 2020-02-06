# method 2: two pointers, time O(n), space O(1)
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if not nums or k <= 0:
            return 0
        cnt = 0
        cur = 1
        start = 0
        for end, num in enumerate(nums):
            cur *= num
            while cur >= k and start <= end:
                cur /= nums[start]
                start += 1
            cnt += end-start+1
        return cnt



# method 1: pre_products, with binary search, O(n*log(n)), sapce O(n)
class Solution1(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k <= 0:
            return 0
        
        pre_products = [1]
        cur = 1
        cnt = 0
        for num in nums:
            cur *= num
            cnt += self.count(pre_products, k, cur)
            pre_products.append(cur)  # don't forget
        return cnt
    
    def count(self, pre_products, k, cur):
        # find the counts that pre_products[i]*k > cur
        left, right = 0, len(pre_products)-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if pre_products[mid]*k <= cur:
                left = mid
            else:
                right = mid
        if pre_products[left]*k > cur:
            return len(pre_products) - left
        elif pre_products[right]*k > cur:
            return len(pre_products) - right
        else:
            return 0


"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
