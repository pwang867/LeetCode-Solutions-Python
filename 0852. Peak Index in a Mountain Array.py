# binary search, time O(log(n)), space O(1)
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return -1
        
        left, right = 0, len(A)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid-1]:
                left = mid
            else:
                right = mid
        
        
