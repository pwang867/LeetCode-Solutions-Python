# time O(n), space O(1), simpler writing


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for i, num in enumerate(nums):
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    

# time O(n), space O(1)


class Solution1(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        for i, num in enumerate(nums):
            if not stack or stack[-1] < num:
                stack.append(num)
            elif len(stack) == 2 and stack[0] < num < stack[1]:
                stack[1] = num
            elif num < stack[0]:
                stack[0] = num
            if len(stack) == 3:
                return True
        return False


"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
"""
