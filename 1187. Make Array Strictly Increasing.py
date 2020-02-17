# dp, similar to Leetcode problem: Arithmetic Slices II - Subsequence
# dp at index i = {the possible value ending in position i: the min operations}
# time: m*n*log(n), space O(n), where m = len(arr1), n = len(arr2)

from collections import defaultdict
import bisect
class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr2.sort()
        
        dp = {-1: 0}  # {ending value: minimum number of operations}
        for cur in arr1:
            temp = defaultdict(lambda: float('inf'))
            for pre in dp:
                # when no replacement
                if cur > pre:
                    temp[cur] = min(temp[cur], dp[pre])  # no operation on cur
                # when we replace cur, greedy, replace arr1 with as small valid
                # value from arr2 as small as possible
                i = bisect.bisect_right(arr2, pre)  
                if i < len(arr2):
                    temp[arr2[i]] = min(temp[arr2[i]], dp[pre]+1)
            dp = temp
            if not dp:
                return -1
        
        return min(dp.values())
    
    
"""
Given two integer arrays arr1 and arr2, return the minimum number of operations 
(possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 
0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.


Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
"""
