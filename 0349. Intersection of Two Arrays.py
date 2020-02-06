# method2, do not use extra space, time O(m*log(m)+n*log(n)), space O(1)
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res = []
        
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if i > 0 and nums1[i] == nums1[i-1]:
                i += 1
            elif j > 0 and nums2[j] == nums2[j-1]:
                j += 1
            else:
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    i += 1
                    j += 1
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
        
        return res
            

# method 1, use set, time O(m+n), space O(m+n)
class Solution1(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1&set2)

        
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""
