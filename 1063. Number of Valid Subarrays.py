# method 2, ascending stack, time/space O(n)


class Solution2(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-float('inf'))
        stack = []
        res = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                res += i - j
            stack.append(i)
        return res


# method 1, brute force, O(n^2)


class Solution1(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i, num in enumerate(nums):
            for j in range(i, len(nums)):
                if nums[i] <= nums[j]:
                    res += 1
                else:
                    break
        return res


"""
Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.



Example 1:

Input: [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
Example 2:

Input: [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].
Example 3:

Input: [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].


Note:

1 <= A.length <= 50000
0 <= A[i] <= 100000
"""
