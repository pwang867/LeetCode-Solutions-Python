# hard to think of

# method 2, improved from method 1
# time O(n), space O(1)
# ref, draw graphs: https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/discuss/489882/O(n)-Solution-with-explanation
class Solution(object):
    def maxValueAfterReverse(self, nums):
        if not nums: return 0
        base = 0
        for i in range(len(nums)-1):
            base += abs(nums[i] - nums[i+1])
        diff = 0
        _max, _min = -float('inf'), float('inf')
        for i in range(len(nums)-1):
            _max = max(_max, min(nums[i], nums[i+1]))
            _min = min(_min, max(nums[i], nums[i+1]))
        diff = max(diff, (_max - _min)*2)    # don't forget the factor 2
        
        # boundary
        for i in range(1, len(nums)-1):
            diff = max(diff, abs(nums[i+1]-nums[0]) - abs(nums[i]-nums[i+1]))
            diff = max(diff, abs(nums[i-1]-nums[-1]) - abs(nums[i-1]-nums[i]))
        
        return base + diff
        

# method 1, brute force, O(n^2), time limit exceeded
class Solution1(object):
    def maxValueAfterReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        base = 0
        for i in range(len(nums)-1):
            base += abs(nums[i+1] - nums[i])
        diff = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                cur = 0
                if i - 1 >= 0:
                    cur += abs(nums[i-1] - nums[j]) - abs(nums[i-1] - nums[i])
                if j + 1 < len(nums):
                    cur += abs(nums[j+1] - nums[i]) - abs(nums[j+1] - nums[j])
                diff = max(diff, cur)
        return diff + base


"""
You are given an integer array nums. The value of this array is defined as the sum of |nums[i]-nums[i+1]| for all 0 <= i < nums.length-1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.

 

Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68
 

Constraints:

1 <= nums.length <= 3*10^4
-10^5 <= nums[i] <= 10^5
Accepted
"""
