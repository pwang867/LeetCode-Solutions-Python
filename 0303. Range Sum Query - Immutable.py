class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = []
        
        total = 0
        for num in nums:
            total += num
            self.sums.append(total)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]  # mistake: - self.sums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
