# there are four possibilities for
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# just choose the max
# abs(A) + abs(B) = max(A+B, A-B, -A+B, -A-B).


class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        if not arr1 or len(arr1) < 2:
            return 0
        mins = self.get_state(arr1, arr2, 0)
        max_val = -float('inf')
        for i in range(1, len(arr1)):
            cur = self.get_state(arr1, arr2, i)
            max_val = max(max_val, max([cur[j] - mins[j] for j in range(4)]))
            mins = [min(mins[j], cur[j]) for j in range(4)]
        return max_val

    def get_state(self, arr1, arr2, i):
        return [i + arr1[i] + arr2[i], i + arr1[i] - arr2[i],
                i - arr1[i] + arr2[i], i - arr1[i] - arr2[i]]


"""
Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 

Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 

Constraints:

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
"""
