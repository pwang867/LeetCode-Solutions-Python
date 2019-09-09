# method 3, do a binary search for i only, j is defined by (m+n)//2 - i
# time O(log(min(m,n))
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):  # to guarantee j = (m + n)//2 - i is valid
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)  # m <= n
        imin, imax = 0, m  # not m-1 because we will consider nums1[i] and nums1[i-1]
        N = (m + n)//2
        
        while imin <= imax:
            i = (imin + imax)//2
            j = N - i
            A1 = nums1[i-1] if i >= 1 else -float('inf')
            A2 = nums1[i] if i < len(nums1) else float('inf')
            B1 = nums2[j-1] if j >= 1 else -float('inf')
            B2 = nums2[j] if j < len(nums2) else float('inf')
            
            if A1 <= B2 and B1 <= A2:
                if (m+n)%2 == 1:
                    return min(A2, B2)
                else:
                    return (min(A2, B2) + max(A1, B1))/2.0
            elif A1 > B2:
                imax = i - 1  # when i == 0, A1=-float('inf'), so we will never have A1 > B2
            elif B1 > A2:
                imin = i + 1
        
        
# method 2, find k-th value, throw k/2 values at each time
# optimize for median of even number, don't have to call subfunction twice
class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return None
        
        m, n = len(nums1), len(nums2)  # m <= n
        
        median = self.findKthValue(nums1, nums2, 0, 0, (m+n+1)//2)
        return median
    
    def findKthValue(self, nums1, nums2, i, j, k):
        # find the k-th value of nums1[i:] + nums2[j:]
        # k=1 means the smallest element
        # nums1 and nums2 can not be both empty
        
        if k == 1:  # stop condition
            val1 = nums1[i] if i < len(nums1) else float('inf')
            val2 = nums2[j] if j < len(nums2) else float('inf')
            if (len(nums1) + len(nums2))%2 == 1:  # odd
                return min(val1, val2)
            else:  # even
                val3 = nums1[i+1] if i+1 < len(nums1) else float('inf')
                val4 = nums2[j+1] if j+1 < len(nums2) else float('inf')
                fourNums = [val1, val2, val3, val4]
                fourNums.sort()
                return (fourNums[0] + fourNums[1])/2.0
        
        block = k//2
        val1 = nums1[i+block-1] if i+block-1 < len(nums1) else float('inf')
        val2 = nums2[j+block-1] if j+block-1 < len(nums2) else float('inf')
        
        if val1 <= val2:  # not val1 < val2, to make sure len(nums1) < len(nums2)
            return self.findKthValue(nums1, nums2, i + block, j, k - block)
        else:
            return self.findKthValue(nums1, nums2, i, j + block, k - block)

        
# method 1, find k-th value, drop about k/2 values at each round
# time O(log(m+n))
class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return None
        
        m, n = len(nums1), len(nums2)  # m <= n
        
        median = self.findKthValue(nums1, nums2, 0, 0, (m+n+1)//2)
        if (m+n)%2 == 0:
            median =(median + 
                     self.findKthValue(nums1, nums2, 0, 0, (m+n+2)//2))/2.0
        return median
    
    def findKthValue(self, nums1, nums2, i, j, k):
        # find the k-th value of nums1[i:] + nums2[j:]
        # k=1 means the smallest element
        # nums1 and nums2 can not be both empty
        
        # early termination
        if i > len(nums1):
            return nums2[j+k-1]
        if j > len(nums2):
            return nums2[i+k-1]
        
        # stop condition
        if k == 1: 
            return min(nums1[i], nums2[j])
        
        block = k//2
        val1 = nums1[i+block-1] if i+block-1 < len(nums1) else float('inf')
        val2 = nums2[j+block-1] if j+block-1 < len(nums2) else float('inf')
        
        if val1 <= val2:  # not val1 < val2, to make sure len(nums1) < len(nums2)
            return self.findKthValue(nums1, nums2, i + block, j, k - block)
        else:
            return self.findKthValue(nums1, nums2, i, j + block, k - block)
        


"""
# https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
"""
