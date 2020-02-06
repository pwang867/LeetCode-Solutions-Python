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
    
    
