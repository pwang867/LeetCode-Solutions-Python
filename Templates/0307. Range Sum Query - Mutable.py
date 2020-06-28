# method 1: Binary indexed tree
# update: time O(log(n)), sumRange: time O(log(n))
# space: O(n)
# i=0 is a dummy for BIT array (self.sums)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # wrong initialization: self.nums = nums
        # then the self.sums won't be initialized
        self.nums = [0]*(len(nums))  
        
        # use binary indexed tree
        self.sums = [0]*(len(nums)+1)  # self.sums save partial sums
        for i in range(len(nums)):   # do not forget this initialization
            self.update(i, nums[i])
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        # i is index in self.nums
        if i < 0 or i >= len(self.nums):
            return
        
        diff = val - self.nums[i]
        cur = i+1  # do not modify i! i will be used in the end again
        while cur < len(self.sums):
            self.sums[cur] += diff
            cur += cur&-cur
            
        self.nums[i] = val   
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # i, j are index in self.nums
        return self.getSum(j) - self.getSum(i-1)
    
    def getSum(self, i):
        # i is index in self.nums
        if i < 0:  # i might be used as -1 by self.sumRange(0, j)
            return 0
        i = min(i, len(self.nums)-1)
        
        res = 0
        cur = i + 1
        while cur > 0:  # wrong: cur >= 0
            res += self.sums[cur]
            cur -= cur&-cur
        
        return res


# method 2, Segment Tree, Version 2 by Huahua
# https://www.youtube.com/watch?v=rYBtViWXYeI


class TreeNode:
    def __init__(self, start, end, sum):
        self.start, self.end, self.sum = start, end, sum
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, nums):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        # return a TreeNode built for nums[start:end+1]
        if start > end:  # do not forget
            return None
        if start == end:
            return TreeNode(start, end, nums[start])
        root = TreeNode(start, end, 0)
        mid = (start + end) // 2
        root.left = self.build_tree(nums, start, mid)
        root.right = self.build_tree(nums, mid + 1, end)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, node, i, val):
        # trick: argument list must need node, otherwise, can not recurse
        if node.start == node.end == i:
            node.sum = val
            return
        mid = (node.start + node.end) // 2
        if i <= mid:
            self.update(node.left, i, val)
        else:
            self.update(node.right, i, val)
        node.sum = node.left.sum + node.right.sum

    def query(self, node, start, end):
        if start <= node.start and end >= node.end:
            return node.sum
        mid = (node.start + node.end) // 2
        if end <= mid:
            return self.query(node.left, start, end)
        elif start > mid:
            return self.query(node.right, start, end)
        else:
            return self.query(node.left, start, mid) \
                   + self.query(node.right, mid + 1, end)


class NumArray2(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.tree = SegmentTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.tree.update(self.tree.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree.query(self.tree.root, i, j)


# method 1, Segment Tree Version 1
# https://www.youtube.com/watch?v=S0Bf9jpgHmQ


class SegmentTree1:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = (self.n << 1) * [0]
        self.build(nums)
        
    def build(self, nums):
        for i in range(self.n):
            self.tree[i+self.n] = nums[i]
            
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
        
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 0:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1
        
    def query(self, i, j):
        res = 0
        i, j = self.n + i, self.n + j
        while i <= j:
            if (i & 1) == 1:
                res += self.tree[i]
                i += 1
            if (j & 1) == 0:
                res += self.tree[j]
                j -= 1
            i >>= 1
            j >>= 1
        return res
        
class NumArray1:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, i: int, val: int) -> None:
        self.st.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.st.query(i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)



"""
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""
