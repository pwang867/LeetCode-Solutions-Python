# method 2, binary search, O(log(n))
# we can further optimize this method by reducing the binary search range to len(arr)/2
import bisect
class Solution2(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return None
        n = len(arr)//4 + 1
        candidates = [n-1, 2*n-1, 3*n-1]
        for i in candidates:
            if i < len(arr) and self.count(arr, i) >= n:
                return arr[i]
        
    def count(self, arr, i):
        left = bisect.bisect_left(arr, arr[i])
        right = bisect.bisect_right(arr, arr[i])
        return right - left
    

# linear scan, O(n)
class Solution1(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return None
        k = len(arr)//4
        for i in range(k, len(arr)):
            if arr[i] == arr[i-k]:
                return arr[i]
        return None



"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""
