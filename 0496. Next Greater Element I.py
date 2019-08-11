class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # findNums is a subset of nums
        
        #  using stack
        stack = []  # numbers stored inside stack will be descending
        next_greater = {}  # {number in findNums: its nextGreaterElement}
        for num in nums:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        ans = []
        for num in findNums:  # subset
            ans.append(next_greater.get(num, -1))
            
        return ans
    
