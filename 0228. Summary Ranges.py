class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        left = 0
        ranges = []
        for right in range(1, len(nums)):
            if nums[right] > nums[right-1] + 1:
                self.addRange(ranges, nums[left], nums[right-1])
                left = right
        self.addRange(ranges, nums[left], nums[-1])  # easy to forget
        return ranges
    
    
    def addRange(self, ranges, left, right):
        if left == right:
            ranges.append(str(left))
        elif left < right:
            ranges.append(str(left) + "->" + str(right))
        
        
