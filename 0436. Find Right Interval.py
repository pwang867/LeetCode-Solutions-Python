# binary search, time O(n*log(n)), space O(n)
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        if not intervals:
            return []
        arr = [(interval[0], interval[1], i) for i, interval in enumerate(intervals)]
        arr.sort()
        res = [0]*len(arr)
        res[arr[-1][-1]] = -1
        for i in range(len(arr)-1):
            k = self.binarySearch(arr, i+1, arr[i][1])  
            res[arr[i][2]] = arr[k][2] if k != -1 else -1   # mistake: res[arr[i][2]] = k
        return res
    
    def binarySearch(self, arr, i, target):
        # return the first index j in arr[i:] that arr[j][0] >= end
        left, right = i, len(arr)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if arr[mid][0] == target:
                return mid
            elif arr[mid][0] > target:
                right = mid
            else:
                left = mid
        
        if arr[left][0] >= target:
            return left
        if arr[right][0] >= target:
            return right
        return -1



"""
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
 

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
 

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
