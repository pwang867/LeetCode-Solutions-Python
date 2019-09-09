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
    
            
            
