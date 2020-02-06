# method 3, based on method 2, but overwrite preorder to save space
# time O(n), space O(1)
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        end = -1
        low = -float('inf')
        for num in preorder:
            if num < low:
                return False
            while end >= 0 and num > preorder[end]:
                low = preorder[end]
                end -= 1
            end += 1             # watch out the order of those two lines
            preorder[end] = num
        return True


# method 2: use stack iteration, time O(n), space O(n)
class Solution2(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        low = -float('inf')
        for num in preorder:
            if num < low:
                return False
            while stack and num > stack[-1]:
                low = stack.pop()
            stack.append(num)
        return True
    

# method 1: divide and conquer, use recursion, (low, high) , time O(n*log(n)), 
# time limit exceeded, space recursion stack O(log(n))
class Solution1(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        return self.verifyHelper(preorder, 0, len(preorder)-1, 
                                 -float('inf'), float('inf'))
    
    def verifyHelper(self, preorder, left, right, low, high):
        if left > right:  # mistake: if left >= right
            return True
        if preorder[left] <= low or preorder[left] >= high:
            return False
        mid = left+1
        while mid <= right and preorder[mid] < preorder[left]:   # time consuming here O(n) for each recursion
            mid += 1
        return self.verifyHelper(preorder, left+1, mid-1, low, preorder[left]) and\
                self.verifyHelper(preorder, mid, right, preorder[left], high)


"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?
"""
