# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """


""" 
method 1: binary search in two steps, find peak first, then search on each side

Based on whether A[i-1] < A[i] < A[i+1], A[i-1] < A[i] > A[i+1], 
or A[i-1] > A[i] > A[i+1], we are either at the left side, peak, 
or right side of the mountain. We can binary search to find the peak. 

After finding the peak, we can binary search two more times 
to find whether the value occurs on either side of the peak.
"""
class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        
        # search peak
        left, right = 0, n-1
        while left + 1 < right:
            mid = left + (right-left)//2
            pre = mountain_arr.get(mid-1)
            cur = mountain_arr.get(mid)
            if cur > pre:
                left = mid
            else:
                right = mid
        peak = left if mountain_arr.get(left) > mountain_arr.get(right) else right
        
        i = self.search(target, mountain_arr, 0, peak, True)
        if i != -1:
            return i
        
        return self.search(target, mountain_arr, peak, n-1, False)
    
    def search(self, target, mountain_arr, left, right, flag=True):
        # flag = True means the array mountain_arr[left:right+1] 
        # is increasing, else decreasing
        while left + 1 < right:
            mid = left + (right - left)//2
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif (flag and cur > target) or (not flag and cur < target):
                right = mid
            else:
                left = mid
        
        if mountain_arr.get(left) == target:
            return left
        if mountain_arr.get(right) == target:
            return right
        return -1
    
            
            
"""
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""
