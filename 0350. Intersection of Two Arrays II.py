from collections import defaultdict
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = defaultdict(int)
        for num in nums1:
            d[num] += 1
            
        res = []
        for num in nums2:
            if num in d and d[num] > 0:
                d[num] -= 1
                res.append(num)
        
        return res
    
    
"""
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
A: binary search
What if nums1's size is small compared to nums2's size? Which algorithm is better?
A: the code above will work great
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
A: sort nums1 and nums2 chuck by chuck first, and then use two pointers
"""
