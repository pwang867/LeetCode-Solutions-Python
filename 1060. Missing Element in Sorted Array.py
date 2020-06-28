# method 2binary search, log(n)


class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 1
        if len(nums) == 1:
            return nums[0] + 1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            missing = (nums[mid] - nums[left]) - (mid - left)
            if missing >= k:
                right = mid
            else:
                left = mid
                k -= missing
        if (nums[right] - nums[left]) - (right - left) >= k:
            return nums[left] + k
        else:
            k -= (nums[right] - nums[left]) - (right - left)
            return nums[right] + k


# method 1, naive line scan, O(n)


"""

Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.



Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""